# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 23:17:47 2019

@author: Ashish.Gupta
"""

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
import pytesseract
#import argparse
import cv2
import numpy as np

#ap = argparse.ArgumentParser()
#ap.add_argument("-i", "--image", required=True,
#	help="path to input image to be OCR'd")
#ap.add_argument("-p", "--preprocess", type=str, default="thresh",
#	help="type of preprocessing to be done")
#args = vars(ap.parse_args())

ImageFile.LOAD_TRUNCATED_IMAGES = True

im = Image.open('D:\Personal\Machine Learning\PAN CARD\pancard7.jpg') # Can be many different formats.

pix = im.load()

# Get the width and hight of the image for iterating over
#print pix[x,y] 
#print (im.size) 


# load the example image and convert it to grayscale
image = cv2.imread('D:\Personal\Machine Learning\PAN CARD\pancard7.jpg')
img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply dilation and erosion to remove some noise
kernel = np.ones((1, 1), np.uint8)
img = cv2.dilate(img, kernel, iterations=1)
img = cv2.erode(img, kernel, iterations=1)

    # Write image after removed noise
cv2.imwrite("removed_noise.png", img)

    #  Apply threshold to get image with only black and white
    #img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)

    # Write the image after apply opencv to do some ...
cv2.imwrite("thres.jpg", img)
pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\Ashish.Gupta\\AppData\\Local\\Tesseract-OCR\\tesseract.exe'
result = pytesseract.image_to_string(Image.open("thres.jpg"))
print(result)
    
    
cv2.imshow('Original image',image)
cv2.imshow('Gray image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
  
  
    
    
    