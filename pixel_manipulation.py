

import cv2
import random

img = cv2.imread('r.png', -1)
print(img.shape)

# pixel manipulation
for i in range(100):
    for j in range(img.shape[1]):
        img[i][j] = [random.randint(0,255), random.randint(0,255),random.randint(0,255)]


# copy & paste
tag = img[500:650, 600:900]
img[100:250, 650:950] = tag 


cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()



