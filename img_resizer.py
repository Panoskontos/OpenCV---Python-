import cv2

# read
img = cv2.imread('r.png', -1)

# resize percentage
img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)

# rotate
img = cv2.rotate(img, cv2.cv2.ROTATE_180)

# # save your altered image
cv2.imwrite('n.png', img)


# print
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


