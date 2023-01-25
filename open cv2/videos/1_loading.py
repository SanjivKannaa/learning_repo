import numpy as np
import cv2

cap = cv2.VideoCapture("video.mp4")

while cap.isOpen():
    ret, frame = cap.read()
    cv2.imshow('video', frame)
    if cv2.waitKey(1) and 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()