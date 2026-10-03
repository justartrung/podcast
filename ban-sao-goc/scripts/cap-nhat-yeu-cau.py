import json
from datetime import datetime, timezone, timedelta
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
p=ROOT/'03-he-thong/cau-hinh-kenh.json'
d=json.loads(p.read_text(encoding='utf-8-sig'))
d['version']=2
d['ending']={'greeting':False,'thanks':False,'goodbye':False,'cta':'topic_specific'}
d['video'].update(trim_repeated_and_error_segments=True,preserve_words_and_meaning=True,thumbnail_intro_seconds=1,subtitle_offset_seconds=1,review_actual_audio_and_video=True)
d['thumbnail']={'width':1080,'height':1920,'background':'black_metallic_gold','title':{'uppercase':True,'font':'serif','colour':'metallic_gold','raised':True,'lines':[2,3],'position':'top','mobile_readable':True},'host':'locked_episode_photo_preserve_face_and_aspect','text_over_face':False,'footer':'COACH MINH THƯ','footer_style':'black_gold_border_soft_gold_glow','separate_text_compositing':True,'regenerate_passed_clips':False}
d['delivery']={'directory':'06-san-sang-dang/{episode_id}','required':['final.mp4','thumbnail.png','caption.txt','subtitles.srt']}
d['facebook'].update(check_cover_selection_actual=True,check_existing_before_retry=True)
d['schedule'].update(require_real_workflow_execution_test=True,heartbeat_reminder_is_sufficient=False,required_conditions=['machine_awake','Codex_app_running','Flow_session_valid','Facebook_Page_session_valid','STOP_off','pilot_verified'])
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
stamp=datetime.now(timezone(timedelta(hours=7))).isoformat()
statepath=ROOT/'03-he-thong/trang-thai.json'
state=json.loads(statepath.read_text(encoding='utf-8-sig'))
state.update(last_updated=stamp,readiness='not_ready',pilot_verified=False,batch_unlocked=False,schedule_enabled=False)
state['blockers']=['flow_tool_cannot_run_after_reopen','observed_flow_price_and_budget_plan','pilot_production_qa_and_post_verification','scheduled_workflow_execution_not_tested']
statepath.write_text(json.dumps(state,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
invpath=ROOT/'03-he-thong/kiem-ke.json'
inv=json.loads(invpath.read_text(encoding='utf-8-sig'))
inv['python_module_search_scope']='python_modules_available/not_found refer to bundled Python; faster-whisper installed in approved asr_python venv'
inv['flow'].update(status='signed_in_exact_tool_cannot_run_after_reopen',evidence='07-bang-chung/flow-mo-lai-van-loi.png',last_checked=stamp)
inv['asr_status']='small_model_reloaded_offline_cpu_int8_av16.0.1_pilot_audio_pending'
invpath.write_text(json.dumps(inv,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
with (ROOT/'05-nhat-ky/events.jsonl').open('a',encoding='utf-8') as f:
    f.write(json.dumps({'at':stamp,'event':'requirements_v2_and_reopen_verified','flow':'still_cannot_run','pilot_generation_ledger_count':0,'thumbnail':'06-san-sang-dang/MT-0001/thumbnail.png','intro_fixture_technical_pass':True,'pilot_verified':False,'schedule_enabled':False},ensure_ascii=False)+'\n')
