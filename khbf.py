# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 20:22:55 2019

@author: Ashish.Gupta
"""

from passporteye import read_mrz
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\Ashish.Gupta\\AppData\\Local\\Tesseract-OCR\\tesseract.exe'
# Process image
mrz = read_mrz("D:\Personal\Machine Learning\Passport\download3.jpg")

# Obtain image
mrz_data = mrz.to_dict()

print(mrz_data['country'])
print(mrz_data['names'])
print(mrz_data['surname'])
print(mrz_data['type'])
print(mrz_data['number'])
print(mrz_data['nationality'])
print(mrz_data['sex'])
print(mrz_data['date_of_birth'])
print(mrz_data['surname'])