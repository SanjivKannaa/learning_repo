import numpy as np
import cv2

img = cv2.imread("image.png", 0) # 0 => greyscale

threshold_value = 100
(t_value, binary_threshold) = cv2.threshold(img, threshold_value, 255, cv2.THRESH_BINARY)

cv2.imshow("binary", binary_threshold)


cv2.waitKey()
cv2.destroyAllWindows()