"""Meaningful state/budget tests in a temporary project; never touch live queue."""
import importlib.util
import json
from pathlib import Path
import tempfile
from types import SimpleNamespace as Args
import unittest

spec = importlib.util.spec_from_file_location('manager', Path(__file__).with_name('quan-ly.py'))
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
LIVE = m.ROOT


class Guards(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        m.ROOT = Path(self.tmp.name)
        for name in ('03-he-thong/cau-hinh-kenh.json', '03-he-thong/trang-thai.json', '03-he-thong/STOP.json'):
            m.save(name, json.loads((LIVE/name).read_text(encoding='utf-8-sig')))
        m.save('04-hang-doi/hang-doi.json', {'version':1, 'episodes':[]})
        for i in range(1,5):
            path = m.ROOT/f'02-host/{i}.png'; path.parent.mkdir(exist_ok=True); path.write_bytes(str(i).encode())
        (m.ROOT/'price.txt').write_text('test only price evidence')
        (m.ROOT/'result.txt').write_text('test only result')
        m.run(Args(command='enqueue', title='Test'))

    def tearDown(self):
        m.ROOT = LIVE
        self.tmp.cleanup()

    def reserve(self, ident='g1', cost=40, scene=1):
        return m.run(Args(command='reserve', episode='MT-0001', scene=scene,
                          cost=cost, generation=ident, price_evidence='price.txt'))

    def resolve(self, ident='g1'):
        return m.run(Args(command='generation-result', episode='MT-0001', generation=ident,
                          result='clip_available', evidence='result.txt'))

    def test_exact_cap_and_pending_spend(self):
        self.reserve(); self.resolve()
        self.reserve('g2',40,2); self.resolve('g2')
        with self.assertRaisesRegex(ValueError, '80-credit'): self.reserve('g3',1,3)
        self.assertEqual(m.cost_total(m.read('04-hang-doi/hang-doi.json')['episodes'][0]),80)

    def test_pending_attempt_blocks_new_and_double_reservation(self):
        self.reserve()
        with self.assertRaises(ValueError): self.reserve()
        with self.assertRaisesRegex(ValueError, 'pending'): self.reserve('g2',1,2)

    def test_retry_cap(self):
        self.reserve(cost=10); self.resolve()
        self.reserve('g2',10); self.resolve('g2')
        with self.assertRaisesRegex(ValueError, 'retry cap'): self.reserve('g3',10)

    def test_stop(self):
        m.run(Args(command='stop',reason='test'))
        with self.assertRaisesRegex(ValueError, 'STOP'): self.reserve()

    def test_changed_host(self):
        (m.ROOT/'02-host/1.png').write_bytes(b'changed')
        with self.assertRaisesRegex(ValueError, 'host image changed'): self.reserve()

    def test_pilot_gate_and_rotation(self):
        with self.assertRaisesRegex(ValueError, 'Pilot'): m.run(Args(command='enqueue',title='Second'))
        state=m.read('03-he-thong/trang-thai.json'); state['pilot_verified']=True
        m.save('03-he-thong/trang-thai.json',state)
        for number in range(2,6):
            e=m.run(Args(command='enqueue',title=f'Test {number}'))
            self.assertEqual(e['host_image'],f'02-host/{((number-1)%4)+1}.png')

    def test_no_publish_without_qa(self):
        with self.assertRaisesRegex(ValueError,'passed QA'):
            m.run(Args(command='begin-publish',episode='MT-0001',scheduled_at='2099-10-01T19:30:00+07:00'))

    def test_unknown_price(self):
        for cost in (0,-1,float('nan'),float('inf')):
            with self.assertRaises(ValueError): self.reserve(cost=cost)

    def pass_fixture_qa(self):
        self.reserve(cost=10);self.resolve()
        p=m.ROOT/'synthetic-master.mp4';p.write_bytes(b'test-fixture-not-real-media')
        m.save('synthetic-qa.json',dict(master=p.name,master_sha256=m.digest(p),
               checks={k:True for k in m.QA_KEYS},evidence_files=['result.txt'],
               reviewed_at='test_only',reviewer='unit_test_fixture'))
        m.run(Args(command='qa',episode='MT-0001',file='synthetic-qa.json'))

    def test_master_change_invalidates_qa(self):
        self.pass_fixture_qa()
        (m.ROOT/'synthetic-master.mp4').write_bytes(b'changed')
        with self.assertRaisesRegex(ValueError,'current master'):
            m.run(Args(command='begin-publish',episode='MT-0001',scheduled_at='2099-10-01T19:30:00+07:00'))

    def test_publish_intent_blocks_blind_retry(self):
        self.pass_fixture_qa()
        a=Args(command='begin-publish',episode='MT-0001',scheduled_at='2099-10-01T19:30:00+07:00')
        m.run(a)
        with self.assertRaisesRegex(ValueError,'earlier intent'):m.run(a)
        self.assertFalse(m.read('03-he-thong/trang-thai.json')['pilot_verified'])

    def test_wrong_time_rejected(self):
        self.pass_fixture_qa()
        with self.assertRaisesRegex(ValueError,'19:30'):
            m.run(Args(command='begin-publish',episode='MT-0001',scheduled_at='2099-10-01T20:00:00+07:00'))

    def test_scheduled_post_does_not_unlock_pilot(self):
        self.pass_fixture_qa()
        m.run(Args(command='begin-publish',episode='MT-0001',scheduled_at='2099-10-01T19:30:00+07:00'))
        cfg=m.read('03-he-thong/cau-hinh-kenh.json')
        e=m.read('04-hang-doi/hang-doi.json')['episodes'][0]
        m.save('synthetic-post.json',dict(permalink='https://www.facebook.com/reel/123',
               page_url=cfg['facebook']['page_url'],page_name=cfg['facebook']['page_name'],
               master_sha256=e['master_sha256'],published=False))
        with self.assertRaisesRegex(ValueError,'not a verified publication'):
            m.run(Args(command='verify-published',episode='MT-0001',file='synthetic-post.json'))
        self.assertFalse(m.read('03-he-thong/trang-thai.json')['pilot_verified'])

    def test_future_evidence_cannot_unlock_pilot(self):
        self.pass_fixture_qa()
        m.run(Args(command='begin-publish',episode='MT-0001',scheduled_at='2099-10-01T19:30:00+07:00'))
        cfg=m.read('03-he-thong/cau-hinh-kenh.json');e=m.read('04-hang-doi/hang-doi.json')['episodes'][0]
        m.save('synthetic-post.json',dict(permalink='https://www.facebook.com/reel/123',
               page_url=cfg['facebook']['page_url'],page_name=cfg['facebook']['page_name'],
               master_sha256=e['master_sha256'],published=True,video_playback_checked=True,
               audio_checked=True,subtitles_checked=True,page_identity_checked=True,
               observed_at='2099-10-01T19:31:00+07:00',published_at='2099-10-01T19:30:00+07:00',screenshot='result.txt'))
        with self.assertRaisesRegex(ValueError,'real past'):
            m.run(Args(command='verify-published',episode='MT-0001',file='synthetic-post.json'))
        self.assertFalse(m.read('03-he-thong/trang-thai.json')['pilot_verified'])


if __name__=='__main__': unittest.main()
