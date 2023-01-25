import numpy as np
import cv2



# rectangle
pic = np.zeros((500, 500, 3), dtype='uint8')
cv2.rectangle(pic, (0, 0), (500, 150), (123, 200, 98), 3, lineType=8, shift=0)

cv2.imshow('rectangle', pic)

cv2.waitKey(0)
cv2.destroyAllWindows()



# line
pic = np.zeros((500, 500, 3), dtype='uint8')
cv2.line(pic, (0, 0), (500, 150), (123, 200, 98))

cv2.imshow('line', pic)

cv2.waitKey(0)
cv2.destroyAllWindows()



# circle
pic = np.zeros((500, 500, 3), dtype='uint8')
cv2.circle(pic, (250, 250), 80, (250, 250, 250))

cv2.imshow('circle', pic)

cv2.waitKey(0)
cv2.destroyAllWindows()
