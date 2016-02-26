from apscheduler.schedulers.blocking import BlockingScheduler
import os
import psycopg2
import urlparse
from moodle import main
from slackclient import SlackClient
from slacker import Slacker


def remind():
     conn = psycopg2.connect(
            database='d',
            user='a',
            password='a',
            host='evq',
            port='21'

        )
     cur = conn.cursor()
     
     cur.execute("SELECT * from users")
     rows = cur.fetchall()
     
     token = "You cant use my token :P"
     slack = Slacker(token)
     
     for row in rows:
     
         data=main(str(row[2]))
  
         channel="#"+str(row[4])
         slack.chat.post_message(channel, str(data),username='moodler')
         
     conn.commit()
     conn.close()
