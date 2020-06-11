from imutils import face_utils
import numpy as np
import dlib
import cv2
from math import hypot

p = "shape_predictor_68_face_landmarks.dat"

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(p)

cap = cv2.VideoCapture(0)

def midpoint(p1, p2):

    return int((p1.x + p2.x)/2), int((p1.y + p2.y)/2)

def eye_blinking_ratio(eye_points, facial_landmarks):
    left = (facial_landmarks.part(eye_points[0]).x, facial_landmarks.part(eye_points[0]).y)
    right = (facial_landmarks.part(eye_points[3]).x, facial_landmarks.part(eye_points[3]).y)
    center_top = midpoint(facial_landmarks.part(eye_points[1]), facial_landmarks.part(eye_points[2]))
    center_bottom = midpoint(facial_landmarks.part(eye_points[5]), facial_landmarks.part(eye_points[4]))
    #hor_line = cv2.line(image, left, right, (255, 0, 0), 2)
    #ver_line = cv2.line(image, center_top, center_bottom, (255, 0, 0), 2)

    hor_line_length = hypot((left[0] - right[0]), (left[1] - right[1]))
    ver_line_length = hypot((center_top[0] - center_bottom[0]), (center_top[1] - center_bottom[1]))

    ratio = hor_line_length / ver_line_length
    return ratio

while True:
    # Getting out image by webcam
    _, image = cap.read()
    # Converting the image to gray scale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # key to give up the app.
    font = cv2.FONT_HERSHEY_DUPLEX
    faces = detector(gray)
    for face in faces:
        x1 = face.left()
        y1 = face.top()
        x2 = face.right()
        y2 = face.bottom()
#        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0),3)

        landmarks = predictor(gray, face)

#       #Detect Blinking
        left_eye_ratio = eye_blinking_ratio([36, 37, 38, 39, 40, 41], landmarks)
        right_eye_ratio = eye_blinking_ratio([42, 43, 44, 45, 46, 47], landmarks)

        blinking_ratio = (left_eye_ratio + right_eye_ratio)/2
        if blinking_ratio > 5.5:
            cv2.putText(image, "BLINKING", (50, 150), font, 3, (0, 0, 255))

        height, width, _ = image.shape
        mask = np.zeros((height, width), np.uint8)

        #Gaze Detection
        left_eye_region = np.array([(landmarks.part(36).x, landmarks.part(36).y),
                                    (landmarks.part(37).x, landmarks.part(37).y),
                                    (landmarks.part(38).x, landmarks.part(38).y),
                                    (landmarks.part(39).x, landmarks.part(39).y),
                                    (landmarks.part(40).x, landmarks.part(40).y),
                                    (landmarks.part(41).x, landmarks.part(41).y)], np.int32)
        cv2.polylines(mask, [left_eye_region], True, (0, 0, 255), 1)
        cv2.fillPoly(mask, [left_eye_region], 255)

        left_eye = cv2.bitwise_and(gray, gray, mask=mask)

        min_x = np.min(left_eye_region[:, 0])
        max_x = np.max(left_eye_region[:, 0])

        min_y = np.min(left_eye_region[:, 1])
        max_y = np.max(left_eye_region[:, 1])

        gray_eye = left_eye[min_y:max_y, min_x:max_x]
        _, threshold_eye = cv2.threshold(gray_eye, 70, 255, cv2.THRESH_BINARY)
        eye = cv2.resize(gray_eye, None, fx=5, fy=5)
        threshold_eye = cv2.resize(threshold_eye, None, fx=5, fy=5)

        cv2.imshow("Eye", eye)
        cv2.imshow("Threshold Eye", threshold_eye)
        cv2.imshow("Left Eye", left_eye)



    cv2.imshow("Output", image)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
