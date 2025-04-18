import cv2
image = cv2.imread("lunar.jpg", cv2.IMREAD_ANYCOLOR)
cv2.imshow("moon", image)
cv2.waitKey()
cv2.destroyallwindow()