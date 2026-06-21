from apscheduler.schedulers.blocking import (
    BlockingScheduler
)

from app.scheduler.jobs import (
    oracle_job
)

scheduler = BlockingScheduler()

scheduler.add_job(

    oracle_job,

    trigger="interval",

    hours=1
)

print(
    "ORACLE Scheduler Started"
)

scheduler.start()