#!/usr/bin/env python3
import os
import PIL
from PIL import Image
currdir=os.listdir()

path2images=r'supplier-data/images'

imgdir=os.listdir(path2images)
print(imgdir)
import glob

imgdir2=glob.glob(path2images+'/*.tiff')
print(imgdir2)
for item in imgdir2:
  itemshort=os.path.basename(item)
  newpath=path2images+'/'+itemshort[:-5]+'.jpeg'
  print("Newpath:",newpath)
  im=Image.open(item).convert("RGB")
  im.resize((600,400)).save(newpath)
