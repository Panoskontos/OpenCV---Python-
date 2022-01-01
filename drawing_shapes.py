# Program to draw shapes

import cv2

# open camera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    width = int(cap.get(3))
    height = int(cap.get(4))
    # draw line
    img = cv2.line(frame, (0,0), (width, height), (0, 0, 255), 10 )
    img = cv2.line(img, (0, height), (width,0),  (0, 0, 255), 10 )
    # draw a rectangle
    img = cv2.rectangle(img, (100, 100), (200,200), (125,125,125), -1)
    # draw a circle
    img = cv2.circle(img, (100,100), 60, (0,0,255), -1)
    font = cv2.FONT_HERSHEY_SIMPLEX
    # draw text
    img = cv2.putText(img, 'Rejected!', (10,  height - 10), font, 1, (0,0,255), 5 , cv2.LINE_AA)

    cv2.imshow('frame', frame)

    # close with q
    if cv2.waitKey(1) == ord('q'):
        break

cap.release() 
cv2.destroyAllWindows()
