 #! /usr/bin/env python3
import os
import requests
import glob

textdir='/data/feedback'

a=os.listdir(textdir)
print(a)
ipaddy="00.00.00.0"
#b=glob.glob(textdir+'\\**.txt')
#print(b)
for file in a:
        newfiledict={}
        file1=textdir+'/'+file
        with open(file1,"r") as newfile:
                itemct=0
                for line in newfile:
                        print(line)
                        if itemct==0:
                                print("This is the title")
                                newfiledict['title']=line
                        elif itemct==1:
                                print("This is the name")
                                newfiledict['name']=line
                        elif itemct==2:
                                print("This is the date")
                                newfiledict['date']=line
                        elif itemct==3:
                                print("This is the feedback")
                                newfiledict['feedback']=line
                        else:
                                print("That's weird, we ran out of itemcts")
                        itemct+=1
        print(newfiledict)
        #response=requests.post("http:///feedback",data=newfiledict)
        #response.raise_for_status()
        response=requests.post('http://'+ipaddy+'/feedback/',data=newfiledict)
        response.raise_for_status()
