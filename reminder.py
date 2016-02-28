from apscheduler.schedulers.blocking import BlockingScheduler
import os
import psycopg2
import urlparse
from moodle import main
from slackclient import SlackClient
import slackweb


slack = slackweb.Slack(url="i_wont_give_you_my_url_:|")



def remind():
     conn = psycopg2.connect(

            database='a',
            user='a',
            password='a',
            host='p',
            port='r'

        )
     cur = conn.cursor()
     
     cur.execute("SELECT * from users")
     rows = cur.fetchall()

     for row in rows:
         mylist = str(row[2]).split(',')
         username = mylist[0]
         encrpyt = mylist[1]
         # decrypt= encrypt + x
         password = decrypt
         batch=mylist[2].upper()
         string=username+","+password+","+batch
         value=main(str(string))
         
         userid=str(row[0])
         username=str(row[1])
         data = "<@"
         data = data.strip()+str(userid)
         data = data.strip()+'|'
         data = data.strip()+str(username)
         data = data.strip()+'>'
         data = data.strip()+':Your comming submission deadlines'+'\n'+str(value)
        
         channelname="@"+username
         slack.notify(text=data, channel=channelname, username="moodler")
     conn.commit()
     conn.close()
