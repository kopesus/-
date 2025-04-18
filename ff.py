import cv2


capture = cv2.VideoCapture(0)
while cv2.waitKey(1) <0:
    ret, frame= capture.read()
    cv2.imshow("Videoframe", frame)
