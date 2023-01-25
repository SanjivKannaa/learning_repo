import numpy as np
import cv2
from numpy.core.fromnumeric import size

pic = np.zeros((500, 500, 3), dtype="uint8")


font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(pic, "TEXT", (100, 100), fontFace=font, fontScale=3, color=(255, 255, 255), thickness=4, lineType=cv2.LINE_8)

cv2.imshow("text", pic)

cv2.waitKey(0)
cv2.destroyAllWindows()