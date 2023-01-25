import numpy as np
import cv2

img = cv2.imread("image.png")

matrix = (7, 7)
blur = cv2.GaussianBlur(img, matrix, 0)

cv2.imshow("GaussianBlurring", blur)


cv2.waitKey()
cv2.destroyAllWindows()