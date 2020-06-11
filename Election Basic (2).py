# import the necessary packages
from PIL import Image
import pytesseract
import argparse
from PIL import Image, ImageFile
import cv2
import os
import re
import io
from xlwt import Workbook
import json
from os import listdir
from os.path import isfile, join
import ftfy

################################################################################################################
############################# Section 1: Initiate the command line interface ###################################
################################################################################################################

pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\Ashish.Gupta\\AppData\\Local\\Tesseract-OCR\\tesseract.exe'

##############################################################################################################
###################### Section 2: Load the image -- Preprocess it -- Write it to disk ########################
##############################################################################################################
x_index = 1
mypath = 'D:\Personal\Machine Learning\PAN CARD'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
files_length = len(onlyfiles)
#print(files_length)

# Workbook is created
wb = Workbook()
# add_sheet is used to create sheet.
sheet1 = wb.add_sheet('Sheet 1')

sheet1.write(0, 0, 'S.No')
sheet1.write(0, 1, 'PAN Card')
sheet1.write(0, 2, 'Name')
sheet1.write(0, 3, 'Father Name')
sheet1.write(0, 4, 'Date of Birth')
sheet1.write(0, 5, 'File Name')
sheet1.write(0, 6, 'Text')


ix=0
while ix < files_length:
   ImageFile.LOAD_TRUNCATED_IMAGES = True
   x="'D:\Personal\Machine Learning\PAN CARD\'"
   dir_path = x.replace("'", "")
   file_path = onlyfiles[ix]
   join_path = join(dir_path, file_path)

# load the example image and convert it to grayscale
   image = cv2.imread(join_path)
   print(join_path)
   gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# check to see if we should apply thresholding to preprocess the
# image

   gray = cv2.threshold(gray, 0, 255,
                         cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

   gray = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)

   gray = cv2.resize(gray, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)

   gray = cv2.resize(gray, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

# make a check to see if blurring should be done to remove noise, first is default median blurring

   gray = cv2.medianBlur(gray, 3)

   gray = cv2.bilateralFilter(gray, 9, 75, 75)

   gray = cv2.GaussianBlur(gray, (5, 5), 0)

# write the grayscale image to disk as a temporary file so we can
# apply OCR to it
   filename = "{}.png".format(os.getpid())
   cv2.imwrite(filename, gray)

   bad_chars = ['~', '`','"', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '{', '}', "'", '[', ']', '|', ':', ';', ',',
                '<', '>', '.', '?', '+', '=', '_']

##############################################################################################################
######################################## Section 3: Running PyTesseract ######################################
##############################################################################################################


# load the image as a PIL/Pillow image, apply OCR, and then delete
# the temporary file
   text = pytesseract.image_to_string(Image.open(filename), lang='eng')
# add +hin after eng within the same argument to extract hindi specific text - change encoding to utf-8 while writing
   os.remove(filename)
# print(text)

# show the output images
# cv2.imshow("Image", image)
# cv2.imshow("Output", gray)
# cv2.waitKey(0)

# writing extracted data into a text file
   text_output = open('outputbase.txt', 'w', encoding='utf-8')
   text_output.write(text)
   text_output.close()

   file = open('outputbase.txt', 'r', encoding='utf-8')
   text = file.read()
# print(text)

# Cleaning all the gibberish text
   text = ftfy.fix_text(text)
   text = ftfy.fix_encoding(text)
#   print(text)
   for i in bad_chars:
       text = text.replace(i, '')
#   print(text)

############################################################################################################
###################################### Section 4: Extract relevant information #############################
############################################################################################################

# Initializing data variable
   name = None
   fname = None
   dob = None
   pan = None
   nameline = []
   dobline = []
   panline = []
   text0 = []
   text1 = []
   text2 = []

# Searching for PAN
   lines = text.split('\n')
   for lin in lines:
     s = lin.strip()
     s = lin.replace('\n', '')
     s = s.rstrip()
     s = s.lstrip()
     text1.append(s)

   text1 = list(filter(None, text1))
# print(text1)


# to remove any text read from the image file which lies before the line 'Income Tax Department'

   lineno = 0  # to start from the first line of the text file.

   for wordline in text1:
    xx = wordline.split('\n')
    if ([w for w in xx if re.search(
            '(INCOMETAXDEPARWENT @|mcommx|INCOME|TAX|GOW|GOVT|GOVERNMENT|OVERNMENT|VERNMENT|DEPARTMENT|EPARTMENT|PARTMENT|ARTMENT|INDIA|NDIA)$',
            w)]):
        text1 = list(text1)
        lineno = text1.index(wordline)
        break

# text1 = list(text1)
    text0 = text1[lineno + 1:]
#print(text0)  # Contains all the relevant extracted text in form of a list - uncomment to check


    def findword(textlist, wordstring):
     lineno = -1
     for wordline in textlist:
        xx = wordline.split()
        if ([w for w in xx if re.search(wordstring, w)]):
            lineno = textlist.index(wordline)
            textlist = textlist[lineno + 1:]
            return textlist
     return textlist


###############################################################################################################
######################################### Section 5: Dishwasher part ##########################################
###############################################################################################################

   try:

    # Cleaning first names, better accuracy
     name = text0[0]
     name = name.rstrip()
     name = name.lstrip()
     name = name.replace("8", "B")
     name = name.replace("0", "D")
     name = name.replace("6", "G")
     name = name.replace("1", "I")
     name = re.sub('[^a-zA-Z] +', ' ', name)

    # Cleaning Father's name
     fname = text0[1]
     fname = fname.rstrip()
     fname = fname.lstrip()
     fname = fname.replace("8", "S")
     fname = fname.replace("0", "O")
     fname = fname.replace("6", "G")
     fname = fname.replace("1", "I")
     fname = fname.replace("\"", "A")
     fname = re.sub('[^a-zA-Z] +', ' ', fname)

    # Cleaning DOB
     dob= re.findall(r'\d{2}[-/|-]\d{2}[-/|-]\d{4}', text)
     dob = dob.rstrip()
     dob = dob.lstrip()
     dob = dob.replace('l', '/')
     dob = dob.replace('L', '/')
     dob = dob.replace('I', '/')
     dob = dob.replace('i', '/')
     dob = dob.replace('|', '/')
     dob = dob.replace('\"', '/1')
     dob = dob.replace(" ", "")

    # Cleaning PAN Card details
     election = re.findall(r'\w{2}[a-zA-Z]\d{6}', text)
#     pan = panline.rstrip()
#     pan = pan.lstrip()
#     pan = pan.replace(" ", "")
#     pan = pan.replace("\"", "")
#     pan = pan.replace(";", "")
#     pan = pan.replace("%", "L")

   except:
     pass

# Making tuples of data
   data = {}
   data['Name'] = name
   data['Father Name'] = fname
   data['Date of Birth'] = dob
   data['Election'] = election
   print(data['Election'])
   print(data['Name'])
   print(data['Father Name'])
   print(data['Date of Birth'])

   ix=ix+1

   sheet1.write(ix + 1, 1, data['PAN'])
   sheet1.write(ix + 1, 2, data['Name'])
   sheet1.write(ix + 1, 3, data['Father Name'])
   sheet1.write(ix + 1, 4, data['Date of Birth'])
   sheet1.write(ix + 1, 5, join_path)
   sheet1.write(ix + 1, 6, text)

wb.save('Election Details.xls')