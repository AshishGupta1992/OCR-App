import cv2
import numpy as np
import imutils

kernel = np.ones((5, 5), np.uint8)


template = cv2.imread('Income Tax Department 3.jpg')
gray_image2 = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
img_erosion2 = cv2.erode(gray_image2, kernel, iterations=1)
img_dilation2 = cv2.dilate(img_erosion2, kernel, iterations=1)
template2 = cv2.Canny(img_dilation2, 50, 200)

(tH, tW) = template2.shape[:2]

#open the main image and convert it to gray scale image
main_image = cv2.imread('pancard11 - Copy.jpg')
gray_image = cv2.cvtColor(main_image, cv2.COLOR_BGR2GRAY)
img_erosion = cv2.erode(gray_image, kernel, iterations=1)
img_dilation = cv2.dilate(img_erosion, kernel, iterations=1)

found = None

for scale in np.linspace(0.2, 1.0, 20)[::-1]:
    # resize the image according to the scale, and keep track
    # of the ratio of the resizing
    resized = imutils.resize(gray_image, width=int(gray_image.shape[1] * scale))
    r = gray_image.shape[1] / float(resized.shape[1])

    # if the resized image is smaller than the template, then break
    # from the loop
    if resized.shape[0] < tH or resized.shape[1] < tW:
        break
    # detect edges in the resized, grayscale image and apply template
    # matching to find the template in the image
    edged = cv2.Canny(resized, 50, 200)
    result = cv2.matchTemplate(edged, template2, cv2.TM_CCOEFF)
    (_, maxVal, _, maxLoc) = cv2.minMaxLoc(result)
    clone = np.dstack([edged, edged, edged])
    cv2.rectangle(clone, (maxLoc[0], maxLoc[1]),
                  (maxLoc[0] + tW, maxLoc[1] + tH), (0, 0, 255), 2)
    cv2.imshow("Visualize", clone)
    cv2.waitKey(0)

    if found is None or maxVal > found[0]:
        found = (maxVal, maxLoc, r)

        # unpack the bookkeeping variable and compute the (x, y) coordinates
        # of the bounding box based on the resized ratio
    (_, maxLoc, r) = found
    (startX, startY) = (int(maxLoc[0] * r), int(maxLoc[1] * r))
    (endX, endY) = (int((maxLoc[0] + tW) * r), int((maxLoc[1] + tH) * r))

    cv2.rectangle(main_image, (startX, startY), (endX, endY), (0, 0, 255), 2)
    cv2.imshow("Image", main_image)
    cv2.waitKey(0)

#cv2.imshow("Template", gray_image)
#cv2.imshow("Template2", template2)

#width, height = template.shape[::-1] #get the width and height

#match the template using cv2.matchTemplate
#match = cv2.matchTemplate(gray_image, template, cv2.TM_CCOEFF_NORMED)
#threshold = 0.6
#position = np.where(match >= threshold) #get the location of template in the image

#for point in zip(*position[::-1]): #draw the rectangle around the matched template#
#   cv2.rectangle(main_image, point, (point[0] + width, point[1] + height), (0, 204, 153), 0)
#cv2.imshow('Template Found', main_image)
cv2.waitKey(0)
cv2.destroyAllWindows()