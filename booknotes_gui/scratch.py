# import os
# currdir=os.path.dirname(__file__)
# notesloc=os.path.dirname(os.path.dirname(os.path.dirname(__file__)))+'\\Local_Data'

# import glob

# desname='bn_{}_{}_*.txt'.format('Mate','0')
# print('Desname',desname)

# despath=notesloc+'\\'+desname
# print('Despath',despath)

# a=glob.glob(despath)

# print(a)
# b=glob.glob(notesloc+'\\bn_Mate_0_*.txt')
# print(b)


import os
import glob
notesloc=os.path.dirname(os.path.dirname(os.path.dirname(__file__)))+'\\Local_Data'
notepath=notesloc+'\\bn_Mate_1_*.txt'

with open(notepath,"r") as newfile:
    pass