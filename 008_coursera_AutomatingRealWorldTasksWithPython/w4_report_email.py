#!/usr/bin/env python3

import os
import datetime
import reports
import emails

path2txt="supplier-data/descriptions"

import glob

txtdir=glob.glob(path2txt+'/*.txt')
print(txtdir)
summary=''
for txt in txtdir:
  with open(txt,"r") as newtxt:
    linect=0
    for line in newtxt:
      if linect==0:
        #This is thj name
        summary=summary+"name: "+line+'<br/>'
        linect=1
      elif linect==1:
        summary=summary+"weight: "+line+'<br/>'+'<br/>'
        linect=9
      else:
        pass
print(summary)
today1=str(datetime.date.today())
today2=today1.split('-')
title="Processed Update on {} {}, {}".format('July',today2[2],today2[0])

if __name__=="__main__":
  print('Title:',title)
  reports.generate_report('/tmp/processed.pdf',title,summary)
  today1=str(datetime.date.today())
  today2=today1.split('-')
  subject="Upload Completed - Online Fruit Store"
  body="All fruits are uploaded to our website successfully. A detailed list is attached to this email."
  message= emails.generate_email("automation@example.com","student-01-e513160a538b@example.com",subject,body,'/tmp/processed.pdf')
  emails.send_email(message)

