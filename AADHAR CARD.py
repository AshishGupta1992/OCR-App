# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 00:22:36 2019

@author: Ashish.Gupta
"""


#pytesseract.pytesseract.tesseract_cmd = "C:\\Users\\Ashish.Gupta\\AppData\\Local\\Tesseract-OCR\\tesseract.exe"

from PIL import Image, ImageFile
import pytesseract
#import argparse
import cv2
import numpy as np
import re
import spacy


#ap = argparse.ArgumentParser()
#ap.add_argument("-i", "--image", required=True,
#	help="path to input image to be OCR'd")
#ap.add_argument("-p", "--preprocess", type=str, default="thresh",
#	help="type of preprocessing to be done")
#args = vars(ap.parse_args())

ImageFile.LOAD_TRUNCATED_IMAGES = True

path='D:\Personal\Machine Learning\AADHAR CARD\download4.jpg'

im = Image.open(path) # Can be many different formats.

pix = im.load()

# Get the width and hight of the image for iterating over
#print pix[x,y] 
#print (im.size) 


# load the example image and convert it to grayscale
image = cv2.imread(path)
img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply dilation and erosion to remove some noise
kernel = np.ones((1, 1), np.uint8)
img = cv2.dilate(img, kernel, iterations=2)
img = cv2.erode(img, kernel, iterations=2)

    # Write image after removed noise
cv2.imwrite("removed_noise.png", img)
bad_chars =['~','`','!','@','#','$','%','^','&','*','(',')','{','}',"'",'[',']','|','‘','"',':',';',',','<','>','.','?','+','=','_']
    #  Apply threshold to get image with only black and white
    #img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)

    # Write the image after apply opencv to do some ...
cv2.imwrite("thres.jpg", img)
pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\Ashish.Gupta\\AppData\\Local\\Tesseract-OCR\\tesseract.exe'
result = pytesseract.image_to_string(Image.open("thres.jpg"))
#print(result)
for i in bad_chars : 
    result = result.replace(i, '') 
new_line = result.split('\n')

#print((result))


#Find DOB Year
dob = re.findall(r'\w{0}[1,2]\w{2}[0-9]',result)
#print(len(dob))
if len(dob)==1 and int(dob[0])>2019:
    dob[0]=""   
print(dob[0])

#FIND AADHAR NUMBER
aadharno = re.findall(r'\w{3}[0-9]\s\w{3}[0-9]\s\w{3}[0-9]',result)
print(aadharno[0])

#Get Person Name


#nlp = spacy.load('en')
#doc = nlp(result)
#for sentence in doc.ents:
#     print(sentence.label_) 


#cv2.imshow('Original image',image)
#cv2.imshow('Gray image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
  
  
    
    
    