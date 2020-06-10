# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 23:52:58 2019

@author: Administrator
"""



from os import listdir
from os.path import isfile, join


#ap = argparse.ArgumentParser()
#ap.add_argument("-i", "--image", required=True,
#	help="path to input image to be OCR'd")
#ap.add_argument("-p", "--preprocess", type=str, default="thresh",
#	help="type of preprocessing to be done")
#args = vars(ap.parse_args())

mypath = 'D:\Personal\Machine Learning\PAN CARD'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

print(onlyfiles[0])


 
dir_path="'D:\Personal\Machine Learning\PAN CARD\'"
x = dir_path.replace("'", "")
file_path = onlyfiles[1]

join_path = join(x,file_path)
print(join_path)
#im = Image.open(join_path) 