from apscheduler.schedulers.blocking import BlockingScheduler
from playlist_cloud_script import run

run()

sched = BlockingScheduler()
sched.add_job(run, 'interval', hours=1)
sched.start()
