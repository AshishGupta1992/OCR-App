# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 18:17:47 2019

@author: Ashish.Gupta
"""

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
#import spacy


#ap = argparse.ArgumentParser()
#ap.add_argument("-i", "--image", required=True,
#	help="path to input image to be OCR'd")
#ap.add_argument("-p", "--preprocess", type=str, default="thresh",
#	help="type of preprocessing to be done")
#args = vars(ap.parse_args())

ImageFile.LOAD_TRUNCATED_IMAGES = True

#path='D:\Personal\Machine Learning\Passport\4.jpg'

im = Image.open('D:\Personal\Machine Learning\Passport\download1.jpg') # Can be many different formats.

pix = im.load()

# Get the width and hight of the image for iterating over
#print pix[x,y] 
#print (im.size) 


# load the example image and convert it to grayscale
image = cv2.imread('D:\Personal\Machine Learning\Passport\download1.jpg')
img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#img = cv2.medianBlur(img, 3)

# Apply dilation and erosion to remove some noise
kernel = np.ones((1, 1), np.uint8)
img = cv2.dilate(img, kernel, iterations=1)
img = cv2.erode(img, kernel, iterations=1)

    # Write image after removed noise
cv2.imwrite("removed_noise.png", img)
bad_chars =['~','`','!','@','#','$','%','^','&','*','(',')','{','}',"'",'[',']','|','‘','"',':',';',',','.','?','+','=','_']
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

print((result))


#Find DOB Year
dob = re.findall(r'\d{2}[-/|-]\d{2}[-/|-]\d{4}',result)
#print(len(dob))
  
#print("Date of Birth",dob[0])
#print("Date of Issue",dob[1])
#print("Date of Expiration",dob[2])


index89 = result.find('<')

#print("Country Code",result[index89+1]+result[index89+2]+result[index89+3])

len_string = len(new_line)


#print(type(new_line))
#x=1 
#for x in len_s:
#    print(x)




#cv2.imshow('Original image',image)
#cv2.imshow('Gray image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
  
  
    
    
    