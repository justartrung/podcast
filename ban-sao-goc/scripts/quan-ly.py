"""Local state guards; external actions stay in the authorized browser workflow."""
import argparse
import hashlib
import json
import math
import os
from pathlib import Path
import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
from datetime import datetime, timezone, timedelta
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

ROOT = Path(__file__).resolve().parents[1]
try:
    TZ = ZoneInfo('Asia/Bangkok')
except ZoneInfoNotFoundError:
    TZ = timezone(timedelta(hours=7), name='Asia/Bangkok')
QA_KEYS = ('family_content', 'host_consistency', 'no_greeting', 'topic_cta',
           'complete_speech', 'cuts_reviewed', 'subtitle_audio_sync', 'technical', 'full_watch_listen',
           'thumbnail_vietnamese_and_face', 'intro_exact_one_second', 'post_intro_audio_subtitle_sync',
           'delivery_bundle_complete')


def now():
    return datetime.now(TZ).isoformat(timespec='seconds')


def read(rel):
    return json.loads((ROOT / rel).read_text(encoding='utf-8-sig'))


def save(rel, value):
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_suffix(path.suffix + '.tmp')
    temp.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    os.replace(temp, path)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def inside(rel):
    path = (ROOT / rel).resolve()
    if not path.is_relative_to(ROOT.resolve()) or not path.is_file():
        raise ValueError('Evidence/master must be an existing file inside project')
    return path


def log(event, **fields):
    path = ROOT / '05-nhat-ky/events.jsonl'
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('a', encoding='utf-8') as stream:
        stream.write(json.dumps(dict(at=now(), event=event, **fields), ensure_ascii=False) + '\n')


def guard():
    if (ROOT / 'STOP.now').exists() or read('03-he-thong/STOP.json')['enabled']:
        raise ValueError('STOP active: no new production or publication')


def episode(queue, episode_id):
    return next(e for e in queue['episodes'] if e['id'] == episode_id)


def cost_total(e):
    # Pending or uncertain generations remain charged conservatively.
    return sum(x['cost'] for x in e['generations'])


def verify_input(e):
    if digest(inside(e['host_image'])) != e['host_sha256']:
        raise ValueError('Locked host image changed')


def verify_qa(e, qa_rel):
    qa = json.loads(inside(qa_rel).read_text(encoding='utf-8-sig'))
    master = inside(qa['master'])
    if digest(master) != qa['master_sha256']:
        raise ValueError('QA does not match current master')
    if any(qa.get('checks', {}).get(k) is not True for k in QA_KEYS):
        raise ValueError('Every quality check must pass')
    if not qa.get('reviewed_at') or not qa.get('reviewer') or not qa.get('evidence_files'):
        raise ValueError('QA requires dated full watch/listen evidence')
    for rel in qa['evidence_files']:
        inside(rel)
    if cost_total(e) > read('03-he-thong/cau-hinh-kenh.json')['flow']['credit_limit_per_episode']:
        raise ValueError('Credit cap exceeded')
    if not e['generations'] or any(x['status'] != 'completed' for x in e['generations']):
        raise ValueError('Unresolved generation ledger; reconcile failures before publication')
    for scene in {x['scene'] for x in e['generations']}:
        if not any(x['scene'] == scene and x.get('result') == 'clip_available' for x in e['generations']):
            raise ValueError('A scene has no available clip')
    return qa


def run(args):
    cfg = read('03-he-thong/cau-hinh-kenh.json')
    state = read('03-he-thong/trang-thai.json')
    queue = read('04-hang-doi/hang-doi.json')
    if args.command == 'status':
        return dict(state=state, stop=read('03-he-thong/STOP.json'), episodes=queue['episodes'])
    if args.command == 'stop':
        save('03-he-thong/STOP.json', dict(enabled=True, reason=args.reason,
                                         updated_at=now(), resume_requires_user=True))
        log('stop', reason=args.reason)
        return {'stopped': True}
    if args.command == 'resume':
        if not args.user_authorized:
            raise ValueError('Resume requires explicit user instruction')
        if (ROOT / 'STOP.now').exists():
            raise ValueError('STOP.now still present; user must clear emergency marker')
        save('03-he-thong/STOP.json', dict(enabled=False, reason=None,
                                         updated_at=now(), resume_requires_user=True))
        log('resume', authorization=args.authorization)
        return {'stopped': False}
    guard()
    if args.command == 'enqueue':
        if queue['episodes'] and not state['pilot_verified']:
            raise ValueError('Pilot must be verified before further episodes')
        number = max([e['number'] for e in queue['episodes']] or [0]) + 1
        image = cfg['host_images'][(number - 1) % 4]
        e = dict(id=f'MT-{number:04d}', number=number, title=args.title,
                 host_image=image, host_sha256=digest(inside(image)), status='draft',
                 created_at=now(), generations=[], qa=None, publication=None)
        queue['episodes'].append(e)
        save('04-hang-doi/hang-doi.json', queue)
        log('enqueued', episode=e['id'], host=image)
        return e
    e = episode(queue, args.episode)
    verify_input(e)
    if args.command == 'reserve':
        if e['status'] not in ('draft', 'producing'):
            raise ValueError('Episode not eligible for generation')
        if not math.isfinite(args.cost) or args.cost <= 0:
            raise ValueError('Observed finite positive price required')
        if args.scene < 1:
            raise ValueError('Scene number must be positive')
        if any(x['id'] == args.generation for x in e['generations']):
            raise ValueError('Generation id already reserved')
        if any(x['status'] == 'reserved' for x in e['generations']):
            raise ValueError('Reconcile pending generation before any further click')
        existing = [x for x in e['generations'] if x['scene'] == args.scene]
        if len(existing) >= 1 + cfg['flow']['max_retries_per_scene']:
            raise ValueError('Scene retry cap reached')
        if cost_total(e) + args.cost > cfg['flow']['credit_limit_per_episode']:
            raise ValueError('80-credit limit would be exceeded')
        inside(args.price_evidence)
        e['generations'].append(dict(id=args.generation, scene=args.scene,
                                    cost=args.cost, status='reserved', at=now(),
                                    price_evidence=args.price_evidence))
        e['status'] = 'producing'
    elif args.command == 'generation-result':
        g = next(x for x in e['generations'] if x['id'] == args.generation)
        if g['status'] != 'reserved':
            raise ValueError('Generation already resolved')
        inside(args.evidence)
        g.update(status='completed', result=args.result, evidence=args.evidence, resolved_at=now())
        # "completed" means the attempt reconciled, not that its clip passed QA.
    elif args.command == 'qa':
        if e['status'] not in ('draft', 'producing', 'qa_passed'):
            raise ValueError('Cannot replace QA during/after publication')
        qa = verify_qa(e, args.file)
        e.update(status='qa_passed', qa=args.file, master_sha256=qa['master_sha256'])
    elif args.command == 'begin-publish':
        if e['status'] != 'qa_passed':
            raise ValueError('Publication requires passed QA and no earlier intent')
        verify_qa(e, e['qa'])
        when = datetime.fromisoformat(args.scheduled_at)
        if when.tzinfo is None:
            raise ValueError('Publication timestamp needs timezone')
        local = when.astimezone(TZ)
        if local.strftime('%H:%M:%S') != '19:30:00':
            raise ValueError('Publication must use 19:30 Asia/Bangkok slot')
        if local < datetime.now(TZ):
            raise ValueError('Missed slot; do not backfill')
        for other in queue['episodes']:
            if (other.get('publication') or {}).get('day') == local.date().isoformat():
                raise ValueError('A publication intent already occupies this day')
        e.update(status='publishing_unknown', publication=dict(day=local.date().isoformat(),
                 scheduled_at=local.isoformat(), intended_page=cfg['facebook']['page_url'],
                 intent_at=now(), master_sha256=e['master_sha256']))
    elif args.command == 'verify-published':
        if e['status'] != 'publishing_unknown':
            raise ValueError('Expected a publication intent')
        proof = json.loads(inside(args.file).read_text(encoding='utf-8-sig'))
        verify_qa(e, e['qa'])
        from urllib.parse import urlparse
        url = urlparse(proof.get('permalink', ''))
        if url.scheme != 'https' or url.hostname not in ('www.facebook.com', 'facebook.com'):
            raise ValueError('Facebook permalink required')
        if not any(part in url.path for part in ('/reel/', '/posts/', '/videos/')):
            raise ValueError('Permalink must point to a specific post/video')
        if proof.get('page_url') != cfg['facebook']['page_url'] or proof.get('page_name') != cfg['facebook']['page_name']:
            raise ValueError('Wrong Page')
        if proof.get('master_sha256') != e['master_sha256']:
            raise ValueError('Publication evidence does not identify QA master')
        required = ('published', 'video_playback_checked', 'audio_checked', 'subtitles_checked', 'page_identity_checked')
        if any(proof.get(k) is not True for k in required):
            raise ValueError('Scheduled/unchecked post is not a verified publication')
        if not proof.get('observed_at') or not proof.get('screenshot'):
            raise ValueError('Dated screenshot evidence required')
        inside(proof['screenshot'])
        posted = datetime.fromisoformat(proof['published_at'])
        if posted.tzinfo is None:
            raise ValueError('Published timestamp requires timezone')
        observed = datetime.fromisoformat(proof['observed_at'])
        if observed.tzinfo is None or not posted <= observed <= datetime.now(TZ):
            raise ValueError('Publication evidence must have real past observation timestamps')
        local = posted.astimezone(TZ)
        if local.date().isoformat() != e['publication']['day'] or local.strftime('%H:%M') != '19:30':
            raise ValueError('Actual post does not match assigned daily slot')
        e['status'] = 'published_verified'
        e['publication'].update(evidence=args.file, permalink=proof['permalink'])
        if e['id'] == state['pilot_episode_id']:
            state.update(pilot_verified=True, batch_unlocked=True,
                         readiness='pilot_verified_schedule_not_enabled')
            save('03-he-thong/trang-thai.json', state)
    save('04-hang-doi/hang-doi.json', queue)
    log(args.command, episode=e['id'], status=e['status'], credits_reserved=cost_total(e))
    return e


def main():
    parser = argparse.ArgumentParser()
    subs = parser.add_subparsers(dest='command', required=True)
    subs.add_parser('status')
    p = subs.add_parser('enqueue'); p.add_argument('--title', required=True)
    p = subs.add_parser('stop'); p.add_argument('--reason', required=True)
    p = subs.add_parser('resume'); p.add_argument('--user-authorized', action='store_true'); p.add_argument('--authorization', required=True)
    for name in ('reserve', 'generation-result', 'qa', 'begin-publish', 'verify-published'):
        p = subs.add_parser(name); p.add_argument('--episode', required=True)
        if name == 'reserve':
            p.add_argument('--scene', type=int, required=True); p.add_argument('--cost', type=float, required=True)
            p.add_argument('--generation', required=True); p.add_argument('--price-evidence', required=True)
        elif name == 'generation-result':
            p.add_argument('--generation', required=True); p.add_argument('--result', choices=('clip_available','failed','not_submitted'), required=True)
            p.add_argument('--evidence', required=True)
        elif name in ('qa', 'verify-published'): p.add_argument('--file', required=True)
        else: p.add_argument('--scheduled-at', required=True)
    args = parser.parse_args()
    if args.command == 'status':
        print(json.dumps(run(args), ensure_ascii=False, indent=2)); return
    # Prevent two concurrent sessions from reserving/publishing against stale state.
    lock = ROOT / '03-he-thong/operation.lock'
    try:
        fd = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    except FileExistsError:
        raise SystemExit('Another operation owns operation.lock; reconcile before proceeding')
    try:
        os.write(fd, str(os.getpid()).encode())
        print(json.dumps(run(args), ensure_ascii=False, indent=2))
    except (ValueError, KeyError, StopIteration) as error:
        print('BLOCKED: ' + str(error), file=sys.stderr)
        raise SystemExit(2)
    finally:
        os.close(fd)
        lock.unlink()


if __name__ == '__main__':
    main()
