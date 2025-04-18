import cv2
src=cv2.imread("lunar.jpg", cv2.IMREAD_COLOR)
x=cv2.flip(src, 0)
xy=cv2.flip(src, -1)
y=cv2.flip(src, 1)

cv2.imshow("src" , src)
cv2.imshow("x" , x)
cv2.imshow("xy" , xy)
cv2.imshow("y" , y)
cv2. waitKey()
cv2. destroyAllWindows

