import pytesseract
import cv2
import numpy as np
from pytesseract import Output
import re
from xlwt import Workbook
from os import listdir
from os.path import isfile, join
from PIL import Image, ImageFile

# import numpy as np

# from PIL import Image, ImageFile

x_index = 1
mypath = 'D:\Personal\Machine Learning\PAN CARD'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
files_length = len(onlyfiles)
print(files_length)

# Workbook is created
wb = Workbook()
# add_sheet is used to create sheet.
sheet1 = wb.add_sheet('Sheet 1', cell_overwrite_ok=True)

#Write Headers to sheet
sheet1.write(0, 0, 'S.No')
sheet1.write(0, 1, 'PAN Number')
sheet1.write(0, 2, 'Date of Birth')
sheet1.write(0, 3, 'File Name')


ixsheet = 0
#print(files_lenth)
while ixsheet < files_length:
   ImageFile.LOAD_TRUNCATED_IMAGES = True
   x="'D:\Personal\Machine Learning\PAN CARD\'"
   dir_path = x.replace("'", "")
   file_path = onlyfiles[ixsheet]
   join_path = join(dir_path, file_path)
   print(join_path)
   im = Image.open(join_path)
# load the example image and convert it to grayscale
   image = cv2.imread(join_path)
   image = cv2.resize(image, (1300, 800))
   h, w, _ = image.shape
   img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply dilation and erosion to remove some noise
   kernel = np.ones((1, 1), np.uint8)
   img = cv2.dilate(img, kernel, iterations=2)
   img = cv2.erode(img, kernel, iterations=2)

   pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\Ashish.Gupta\\AppData\\Local\\Tesseract-OCR\\tesseract.exe'

   f = pytesseract.image_to_data(img, output_type=Output.DICT)


# Unique elements in block_num
   new_list = set(f['block_num'])
   my_new_list = list(new_list)

#print(my_new_list)

   new_list1 = set(f['line_num'])
   my_new_list1 = list(new_list1)

#print(my_new_list1)


# Find position of all the elements
   def getIndexPositions_2(listOfElements, element):
    ''' Returns the indexes of all occurrences of give element in
    the list- listOfElements '''
    indexPosList = []
    for i in range(len(listOfElements)):
        if listOfElements[i] == element:
            indexPosList.append(i)
    return indexPosList


   f['conf'] = [int(i) for i in f['conf']]

# Iterate over loops of lines in image
   for x in my_new_list:
    indexPos1 = getIndexPositions_2(f['block_num'], x)

    new_line_list = []

    for ydf in indexPos1:

        if f['line_num'][ydf] not in new_line_list:
            new_line_list.append(f['line_num'][ydf])
    #print("New List")
    #print(new_line_list)
    for xyz in new_line_list:
        indexPos2 = getIndexPositions_2(f['line_num'], xyz)

        iter_list = (list(set(indexPos1).intersection(indexPos2)))
        text = ''
        for y1 in iter_list:
            if f['text'][y1]!='':
                    text = text + f['text'][y1]+' '

        r1 = re.findall(r'\d{2}[-/|-]\d{2}[-/|-]\d{4}', text)
        r2 = re.findall(r'\w{2}[a-zA-Z]\w{0}[P,C,H,A,B,G,J,L,F,T]\w{0}[A-Z]\w{3}[0-9]\w{0}[A-Z]', text)
        if r1:
            sheet1.write(ixsheet+1, 2, r1[0])

        if r2:
            sheet1.write(ixsheet+1, 1, r2[0])
    ixsheet = ixsheet + 1

wb.save('PAN CARD DATA.xls')




