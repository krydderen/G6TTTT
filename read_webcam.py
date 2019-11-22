
import cv2
import numpy as np

cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()

    roi = frame[170:330, 275:438]

    tiles = [roi[0:42, 0:48],
             roi[0:42, 60:105],
             roi[0:42, 120:160],
             roi[55:100, 0:48],
             roi[55:100, 60:105],
             roi[55:100, 120:160],
             roi[115:155, 0:45],
             roi[115:155, 60:105],
             roi[115:155, 120:160]]

    res = cv2.resize(roi, None, fx=3, fy=3, interpolation=cv2.INTER_CUBIC)

    cv2.imshow("frame", res)
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
