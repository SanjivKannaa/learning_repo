import numpy as np
import cv2

cap = cv2.VideoCapture("video.mp4")
fourcc = cv2.VideoWriter_fourcc(*'XVID')
fps = 30
framesize = (720, 480)
out = cv2.VideoWriter('video.avi', fourcc, fps, framesize)

while cap.isOpen():
    ret, frame = cap.read()
    cv2.imshow('video', frame)
    if cv2.waitKey(1) and 0xFF == ord('q'):
        break


out.release()
cap.release()
cv2.destroyAllWindows()