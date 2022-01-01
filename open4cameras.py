
# Program to open 4 cameras


import numpy as np
import cv2


# open camera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    width = int(cap.get(3))
    height = int(cap.get(4))
    
    cv2.imshow('frame', frame)

    # close with q
    if cv2.waitKey(1) == ord('q'):
        break

cap.release() 
cv2.destroyAllWindows()
