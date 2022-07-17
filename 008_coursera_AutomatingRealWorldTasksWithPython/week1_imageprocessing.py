#!/usr/bin/env python3
import os
import glob
from PIL import Image
currdir=os.path.dirname(__file__)
#print(currdir)
savepath=r'/opt/icons/'


imgdir=glob.glob(currdir+'/images/*')
#print(imgdir)

a=os.listdir(currdir+'/images')

for img in imgdir:
        newim=Image.open(img)
        #newim.show()
        newim=newim.convert("RGB")
        #newim.show()
        finalresting=savepath+os.path.basename(img)+'.jpg'
        #print(img)
        #print(finalresting)
        newim.rotate(270).resize((128,128)).save(finalresting)
        #newim.show()
