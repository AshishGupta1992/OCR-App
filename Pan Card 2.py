
#pytesseract.pytesseract.tesseract_cmd = "C:\\Users\\Ashish.Gupta\\AppData\\Local\\Tesseract-OCR\\tesseract.exe"

from PIL import Image, ImageFile
import pytesseract
#import argparse
import cv2
import numpy as np
import re

#ap = argparse.ArgumentParser()
#ap.add_argument("-i", "--image", required=True,
#	help="path to input image to be OCR'd")
#ap.add_argument("-p", "--preprocess", type=str, default="thresh",
#	help="type of preprocessing to be done")
#args = vars(ap.parse_args())

ImageFile.LOAD_TRUNCATED_IMAGES = True

im = Image.open('D:\Personal\Machine Learning\PAN CARD\pancard11.jpg') # Can be many different formats.

pix = im.load()

# Get the width and hight of the image for iterating over
#print pix[x,y] 
#print (im.size) 


# load the example image and convert it to grayscale
image = cv2.imread('D:\Personal\Machine Learning\PAN CARD\pancard11.jpg')
img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply dilation and erosion to remove some noise
kernel = np.ones((1, 1), np.uint8)
img = cv2.dilate(img, kernel, iterations=2)
img = cv2.erode(img, kernel, iterations=2)

    # Write image after removed noise
cv2.imwrite("removed_noise.png", img)
bad_chars =['~','`','!','@','#','$','%','^','&','*','(',')','{','}',"'",'[',']','|',':',';',',','<','>','.','?','/','+','=','_']
    #  Apply threshold to get image with only black and white
    #img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)

    # Write the image after apply opencv to do some ...
cv2.imwrite("thres.jpg", img)
pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\Ashish.Gupta\\AppData\\Local\\Tesseract-OCR\\tesseract.exe'
result = pytesseract.image_to_string(Image.open("thres.jpg"))
#print(result)
for i in bad_chars : 
    result = result.replace(i, '') 
#new_line = result.split('\n')

print((result))



#r'\d{5}[a-zA-Z]\d{5}[a-zA-Z0-9]'
#[a-zA-Z0-9]{10,}


r1 = re.findall(r'\w{2}[a-zA-Z]\w{0}[P,C,H,A,B,G,J,L,F,T]\w{0}[A-Z]\w{3}[0-9]\w{0}[A-Z]',result)

#print(r1)

#for element in result:
#    m = re.match("[a-zA-Z]{5,}", element)
#    if m:
#        print("START:", element)

l = [x for x in result if x.strip()] 

#l = [w.replace(')', '') for w in l]

#print(l)
#cv2.imshow('Original image',image)
#cv2.imshow('Gray image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
  
  
    
    
    