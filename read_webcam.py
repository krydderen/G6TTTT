    cv2.imshow("frame", frame)
import cv2
import numpy as np

cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()

    roi = frame[80:386, 168:470]

    tiles = [roi[0:100, 0:100],
             roi[0:100, 100:200],
             roi[0:100, 200:300],
             roi[100:200, 0:100],
             roi[100:200, 100:200],
             roi[100:200, 200:300],
             roi[200:300, 0:100],
             roi[200:300, 100:200],
             roi[200:300, 200:300]]

    
    cv2.imshow("frame", roi)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
