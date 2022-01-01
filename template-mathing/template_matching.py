import numpy as np
import cv2

# our algorithm requires grayscale images
img = cv2.imread('template-mathing/football.jpg',0)
img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
template = cv2.imread('template-mathing/shoe.png',0)
h, w = template.shape

methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
            cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

for method in methods:
    img2 = img.copy()
    result = cv2.matchTemplate(img2, template, method)
    # find ball location
    minval, maxval, minloc, maxloc = cv2.minMaxLoc(result)
    
    #some methods work differently
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = minloc
    else: 
        location = maxloc

    bottom_right = (location[0]+w, location[1]+h)
    cv2.rectangle(img2, location, bottom_right, 255, 5)
    cv2.imshow('Match', img2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()