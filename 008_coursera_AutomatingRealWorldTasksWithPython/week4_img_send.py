#!/usr/bin/env python3

import requests
import glob
url="http://localhost/upload/"
path2images=r'supplier-data/images'
imgdir3=glob.glob(path2images+'/*.jpeg')
for img in imgdir3:
  with open(img,'rb') as openedimg:
    r=requests.post(url,files={'file': openedimg})
