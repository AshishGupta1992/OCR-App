import pytesseract
import cv2
import numpy as np
from pytesseract import Output

# import numpy as np

# from PIL import Image, ImageFile


# load the example image and convert it to grayscale
image = cv2.imread('D:\Personal\Machine Learning\PAN CARD\pancard6.jpg')
image = cv2.resize(image, (1300, 800))
h, w, _ = image.shape
img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply dilation and erosion to remove some noise
kernel = np.ones((1, 1), np.uint8)
img = cv2.dilate(img, kernel, iterations=2)
img = cv2.erode(img, kernel, iterations=2)

pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\Ashish.Gupta\\AppData\\Local\\Tesseract-OCR\\tesseract.exe'

f = pytesseract.image_to_data(img, output_type=Output.DICT)
print(type(f))

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

    #print(x)
    #print(indexPos1)
    new_line_list = []
    for ydf in indexPos1:
        if f['line_num'][ydf] not in new_line_list:
            new_line_list.append(f['line_num'][ydf])
    #print("New List")
    #print(new_line_list)
    for xyz in new_line_list:
        indexPos2 = getIndexPositions_2(f['line_num'], xyz)

        iter_list = (list(set(indexPos1).intersection(indexPos2)))
        for y1 in iter_list:
                #print(y, y1)
                #print(f['text'][y1])
                zeroth_element = y1
                #    print((zeroth_element))

                minimum_left = f['left'][zeroth_element]
                minimum_top = f['top'][zeroth_element]
                maximum_width = f['width'][zeroth_element]
                maximum_height = f['height'][zeroth_element]
                #            print(xyz)
                #            print(indexPos2)

                # print(y, y1)
                #        indexPos2 = getIndexPositions_2(f['block_num'],x)
                if f['conf'][xyz] > 0:

                    if maximum_width < f['width'][xyz]:
                        maximum_width = f['width'][xyz]

                    if maximum_height < f['height'][xyz]:
                        maximum_height = f['height'][xyz]

                    if minimum_top > f['top'][xyz]:
                        minimum_top = f['top'][xyz]

                    if minimum_left > f['left'][xyz]:
                        minimum_left = f['left'][xyz]
        print(x, xyz)
        print(minimum_left, minimum_top, maximum_width, maximum_height)

        cv2.rectangle(img, (minimum_left, minimum_top),
                      (minimum_left + maximum_width, minimum_top + maximum_height), (0, 255, 0), 2)
        new_img = img[minimum_top:minimum_top + maximum_height, minimum_left:minimum_left + maximum_width]
        d = pytesseract.image_to_string(new_img, output_type=Output.DICT)
        print((d))
        cv2.imshow('img', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()




