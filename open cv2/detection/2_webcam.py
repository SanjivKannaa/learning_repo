import cv2
import numpy as mp

#https://github.com/Itseez/opencv/tree/master/data/haarcascades
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('image.png')
videocapture = cv2.VideoCapture(0)
scale_factor = 1.3

while True:
    ret, pic = videocapture.read()
    faces = face_cascade.detectMultiScale(img, scale_factor, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, 'name', (x, y), font, 2, (255, 255, 255), 2, cv2.LINE_AA)
    print("number of faces found = ", len(faces))
    cv2.imshow('face', img)
    k = cv2.waitKey(30) & 0xFF
    if k == 2:
        break
cv2.destroyAllWindows()