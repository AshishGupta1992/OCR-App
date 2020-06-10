# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""



import cv2


img = cv2.imread('D:\Personal\Machine Learning\PAN CARD\pancard3.jpg')
greyscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
contours= cv2.findContours(greyscaled, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    
#    print(contours)
#    print(hierarchy)
    
cv2.drawContours(img, contours, -1, (0, 0, 255), 2)

cv2.imshow('original',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
