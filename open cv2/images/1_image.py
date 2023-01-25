import cv2

img = cv2.imread("image.png")
cv2.imshow("python", img)
cv2.imwrite("img2.png", img)
cv2.waitKey()