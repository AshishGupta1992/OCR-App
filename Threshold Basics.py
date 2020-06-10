# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 14:02:33 2019

@author: Ashish.Gupta
"""

import cv2


img = cv2.imread('D:\Personal\Machine Learning\PAN CARD\pancard3.jpg')
retval, threshold = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)
greyscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

gaus = cv2.adaptiveThreshold(greyscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

retval2, otsu = cv2.threshold(greyscaled, 100, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

cv2.imshow('original',img)
cv2.imshow('threshold',threshold)
cv2.imshow('gaus',gaus)
cv2.imshow('gaus',otsu)
cv2.waitKey(0)
cv2.destroyAllWindows()
