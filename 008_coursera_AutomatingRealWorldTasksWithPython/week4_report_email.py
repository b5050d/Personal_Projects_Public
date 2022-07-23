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
    for line in txt:
      if linect==0:
        #This is thje name
        summary=summary+"name: "+line+'\n'
        linect=1
      elif linect==1:
        summary=summary+"weight: "+line+'\n\n'
print(summary)

title="Processed Update on "+str(datetime.date.today())

if __name__=="__main__":
  reports.generate_report('/tmp/processed.pdf',title,summary)
  emails.generate_email("automation@example.com","username@example.com",



