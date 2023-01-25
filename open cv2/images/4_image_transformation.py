import numpy as np
import cv2

img = cv2.imread("image.png")
cols = img.shape[1]
rows = img.shape[0]

M = np.float32([[1, 0, 150], [0, 1, 150]])

shifted = cv2.warpAffine(img, M, (cols, rows))
cv2.imshow("shifted", shifted)


cv2.waitKey()
cv2.destroyAllWindows()