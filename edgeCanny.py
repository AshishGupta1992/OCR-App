import cv2
import numpy as np
import imutils


def auto_canny(image, sigma=0.33):
    # compute the median of the single channel pixel intensities
    v = np.median(image)

    # apply automatic Canny edge detection using the computed median
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    edged = cv2.Canny(image, lower, upper)

    # return the edged image
    return edged


template = cv2.imread('Income Tax Department 3.jpg')
gray_image2 = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
blurred2 = cv2.GaussianBlur(gray_image2, (3, 3), 0)
tight2 = cv2.Canny(blurred2, 225, 250)

# open the main image and convert it to gray scale image
main_image = cv2.imread('pancard11 - Copy.jpg')
gray_image = cv2.cvtColor(main_image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray_image, (3, 3), 0)
wide = cv2.Canny(blurred, 10, 200)

width, height = tight2.shape[::-1] #get the width and height

#match the template using cv2.matchTemplate
match = cv2.matchTemplate(wide, tight2, cv2.TM_CCOEFF_NORMED)
threshold = 0.6
position = np.where(match >= threshold) #get the location of template in the image

for point in zip(*position[::-1]): #draw the rectangle around the matched template
   cv2.rectangle(main_image, point, (point[0] + width, point[1] + height), (0, 204, 153), 0)
cv2.imshow('Template Found', main_image)

cv2.imshow("Main Image", wide)
cv2.imshow("Template", tight2)

# cv2.imshow("Template2", tight)
cv2.waitKey(0)
cv2.destroyAllWindows()
