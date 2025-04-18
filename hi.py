import cv2
src = cv2.imread("lunae.jpg", cv2.IMREAD_COLOR)
dst= src.copy()
roi = src[0:80, 100:200]
dst[0:80, 0:100] = roi
cv2.imshow("src" , src)
cv2.imshow("dst" , dst)