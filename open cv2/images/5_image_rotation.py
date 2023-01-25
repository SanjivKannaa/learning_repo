import numpy as np
import cv2

img = cv2.imread("image.png")
cols = img.shape[1]
rows = img.shape[0]
center = (cols/2, rows/2)
angle = 90
M = cv2.getRotationMatrix2D(center, angle, 1) #1 is the size factor

rotated = cv2.warpAffine(img, M, (cols, rows))
cv2.imshow("rotated", rotated)


cv2.waitKey()
cv2.destroyAllWindows()