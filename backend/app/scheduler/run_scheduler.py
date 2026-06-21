from apscheduler.schedulers.blocking import (
    BlockingScheduler
)

from app.scheduler.jobs import (
    collect_trends
)

scheduler = (
    BlockingScheduler()
)

scheduler.add_job(

    collect_trends,

    "interval",

    minutes=5
)

print(
    "ORACLE Scheduler Started"
)

scheduler.start()