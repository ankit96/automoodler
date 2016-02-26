from apscheduler.schedulers.blocking import BlockingScheduler
import os
import subprocess
import psycopg2
import urlparse
from moodle import main
from slackclient import SlackClient
from reminder import remind
import logging
logging.basicConfig()
sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='mon-sun', hour=7 , minute=55)
def scheduled_job():
    remind()

sched.start()

while __name__ == '__main__':
  pass
