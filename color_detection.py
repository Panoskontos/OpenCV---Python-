import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))


    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lowblue = np.array([90,50,50])
    updblue = np.array([130,255,255])


    mask = cv2.inRange(hsv, lowblue, updblue)
    
    # blend 2 images together, comparing bits for blue
    result = cv2.bitwise_and(frame, frame, mask=mask)


    cv2.imshow('frame', result)
    cv2.imshow('frame', mask)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()