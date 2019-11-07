    cv2.imshow("frame", frame)
import cv2
import numpy as np

cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()

    roi = frame[90:370, 180:470]

    tiles = [roi[0:80, 0:80],
             roi[0:80, 100:180],
             roi[0:80, 205:285],
             roi[100:180, 0:100],
             roi[100:180, 100:180],
             roi[100:180, 205:285],
             roi[200:275, 0:100],
             roi[200:275, 100:180],
             roi[200:275, 205:285]]

    cv2.imshow("frame", roi)
    cv2.imshow("1", tiles[0])
    cv2.imshow("2", tiles[1])
    cv2.imshow("3", tiles[2])
    cv2.imshow("4", tiles[3])
    cv2.imshow("5", tiles[4])
    cv2.imshow("6", tiles[5])
    cv2.imshow("7", tiles[6])
    cv2.imshow("8", tiles[7])
    cv2.imshow("9", tiles[8])


    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
