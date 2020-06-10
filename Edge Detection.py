# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 13:04:03 2019

@author: Ashish.Gupta
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 21:19:29 2019

@author: Administrator
"""

#pytesseract.pytesseract.tesseract_cmd = "C:\\Users\\Ashish.Gupta\\AppData\\Local\\Tesseract-OCR\\tesseract.exe"

from PIL import Image, ImageFile

#import argparse
import cv2


#ap = argparse.ArgumentParser()
#ap.add_argument("-i", "--image", required=True,
#	help="path to input image to be OCR'd")
#ap.add_argument("-p", "--preprocess", type=str, default="thresh",
#	help="type of preprocessing to be done")
#args = vars(ap.parse_args())

ImageFile.LOAD_TRUNCATED_IMAGES = True

im = Image.open('D:\Personal\Machine Learning\PAN CARD\pancard2.jpg') # Can be many different formats.

pix = im.load()

# Get the width and hight of the image for iterating over
#print pix[x,y] 
#print (im.size) 


# load the example image and convert it to grayscale
image = cv2.imread('D:\Personal\Machine Learning\PAN CARD\pancard2.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#img=cv2.resize(image,(720,480))
#print (image.size)
#print image[x,y]
#cv2.imshow('Original image',image)
#cv2.imshow('Gray image', gray)
ret,    thresh = cv2.threshold(gray,127,255,0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    
print("No of Contours=" + str(len(contours)))
cv2.drawContours(image, contours, -1, (0,255,0),3)
#for x in range(len(contours)):
#   print(contours[x])

#gray = cv2.medianBlur(gray, 3)
#gray = cv2.threshold(gray, 0, 255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

#for cnt in contours:
#    rect = cv2.minAreaRect(cnt)
#    box = cv2.boxPoints(rect)
#    img = cv2.drawContours(thresh, [box],0,(0,255,0),3)

cv2.imshow('Original image',image)
cv2.imshow('Gray image', gray)

cv2.waitKey(0)
cv2.destroyAllWindows()
  
  
    
    
    