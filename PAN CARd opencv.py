# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 21:19:29 2019

@author: Administrator
"""

#pytesseract.pytesseract.tesseract_cmd = "C:\\Users\\Ashish.Gupta\\AppData\\Local\\Tesseract-OCR\\tesseract.exe"

from PIL import Image, ImageFile
import pytesseract
#import argparse
import cv2
import os
import re
from xlwt import Workbook 


#ap = argparse.ArgumentParser()
#ap.add_argument("-i", "--image", required=True,
#	help="path to input image to be OCR'd")
#ap.add_argument("-p", "--preprocess", type=str, default="thresh",
#	help="type of preprocessing to be done")
#args = vars(ap.parse_args())

ImageFile.LOAD_TRUNCATED_IMAGES = True

im = Image.open('D:\Personal\Machine Learning\PAN CARD\pancard10.jpg') # Can be many different formats.

pix = im.load()

# Get the width and hight of the image for iterating over
#print pix[x,y] 
#print (im.size) 


# load the example image and convert it to grayscale
image = cv2.imread('D:\Personal\Machine Learning\PAN CARD\pancard10.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#print (image.size)
#print image[x,y]
#cv2.imshow('Original image',image)
#cv2.imshow('Gray image', gray)
gray = cv2.medianBlur(gray, 3)
#gray = cv2.threshold(gray, 0, 255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]


filename = "{}.png".format(os.getpid())
cv2.imwrite(filename, gray)



pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\Ashish.Gupta\\AppData\\Local\\Tesseract-OCR\\tesseract.exe'
text = pytesseract.image_to_string(Image.open(filename))
os.remove(filename)
#print(type(text))
x = text.replace("/", "")
y = x.replace("-", " ") 

data = y.split() #split string into a list


#convert it to upper case
data = [element.upper() for element in data]
#out = map(lambda x:x.upper(), data)

#PAN CARD text
#for temp in out:
#   print(temp)
   
  
#print(type(data))
   
#permanent_list = 'NAME'
#account_list = 'ACCOUNT'
#number_list = 'NUMBER'


if any("PERMANENT" in s for s in data):
    permanent_list = data.index("PERMANENT")
    #print(data.index("PERMANENT"))

if any("ACCOUNT" in s for s in data):
  account_list = data.index("ACCOUNT")
  

if any("NUMBER" in s for s in data):
  num_list = data.index("NUMBER")
  


  
#if number_list in out :
#    print(out.index(number_list))
  
#print(permanent_list)
#print(account_list)
#print(number_index)

#Getting PAN NUmber
if (permanent_list-account_list)==-1:
    PAN_NO = permanent_list + 3
    print(data[PAN_NO])
  

#Getting Date
r1 = re.findall(r'\d{2}[-/]\d{2}[-/]\d{4}',text)
#print("Empty String!")

# Workbook is created 
wb = Workbook() 


# add_sheet is used to create sheet. 
sheet1 = wb.add_sheet('Sheet 1')

#Write Headers to sheet
sheet1.write(0, 0, 'S.No')
sheet1.write(0, 1, 'PAN Number')
sheet1.write(0, 2, 'Date of Birth')

#Write data to sheet

sheet1.write(1, 0, '1')
sheet1.write(1, 1, data[PAN_NO])
if not r1:
    sheet1.write(1, 2, '')
else:    
    sheet1.write(1, 2, r1[0])
 


wb.save('xlwt example.xls') 
  
  
    
    
    