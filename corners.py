import numpy as np
import cv2

img = cv2.imread('vegeta.png')
img = cv2.resize(img, (0,0), fx=0.75, fy=0.75)

# find the corners on our grey image
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 20 is number of lines, 10 is euclidian distance
corners = cv2.goodFeaturesToTrack(grey, 20, 0.01, 10 )

# covert corvers array into integers
corners = np.int0(corners)
for corner in corners:
    x, y = corner.ravel() 
    # draw circle in every corner
    cv2.circle(img, (x, y), 5, (255,0,0), -1)

# create a graph from corners
for i in range(len(corners)):
    for j in range(len(corners)):
        corner1 = tuple(corners[i][0])
        corner2 = tuple(corners[j][0])
        # draw a line
        # when you want to write 1 line functions write lambda
        color = tuple(map(lambda x: int(x),np.random.randint(0, 255, size=3)))
        cv2.line(img, corner1, corner2, color, 1)





cv2.imshow('Frame', img)
cv2.waitKey(0)
cv2.destroyAllWindows()