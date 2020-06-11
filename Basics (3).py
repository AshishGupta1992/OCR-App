import cv2
import numpy as np

#Load YOLO

net = cv2.dnn.readNet("yolov3.weights", "yolo.cfg")
classes = []
with open("coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]

layers_names = net.getLayerNames()
outputlayers = [layers_names[i[0]-1] for i in net.getUnconnectedOutLayers()]

#loading image
img = cv2.imread("images.jpg")
cv2.imshow("Image", img)
height, width, channel = img.shape

#detecting objects
blob = cv2.dnn.blobFromImage(img, 0.00392, (416,416), (0, 0, 0), True)

for b in blob:
    for n, img_blob in enumerate(b):
        cv2.imshow(str(n), img_blob)

net.setInput(blob)
outs = net.forward(outputlayers)

for out in outs:
    for detection in out:
        scores = detection[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]
        if confidence > 0.5:
            center_x = int(detection[0] * width)
            center_y = int(detection[1] * height)
            w = int(detection[2] * width)
            h = int(detection[3] * height)

            x = int(center_x-w/2)
            y = int(center_y-h/2)


            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)


cv2.waitKey(0)
cv2.destroyAllWindows()