
#! /usr/bin/env python3

import os
import requests

path2txt='supplier-data/descriptions/'

import glob

txtdir=glob.glob(path2txt+'*.txt')
for txt in txtdir:
  with open(txt,"r") as rtxt:
    newdict={}
    linect=0
    for line in rtxt:
      print(line)
      if linect==0:
        newdict["name"]=line[:-1]
      elif linect==1:
        newdict["weight"]=int(line[:-5])
      elif linect==2:
        newdict["description"]=line[:-1]
      linect+=1
  newdict["image_name"]=os.path.basename(txt)[:-4]+'.jpeg'
  print(newdict)
  response=requests.post('http://34.134.45.186/fruits/',newdict)
  response.raise_for_status()



