import numpy as np
import cv2

img = cv2.imread('thomas.jpg', cv2.IMREAD_COLOR)

img[55, 55] = [255, 255, 255]
px = img[55, 55] # Location of the pixel in image.

print(px) # Prints color value of the pixel.


# REGION OF INTEREST In IMAGE.
roi = img[100:150, 100:150]
# print(roi)

img[100:150, 100:150] = [255, 0, 0]

face = img[37:111, 107:194]
img[0:74, 0:87] = face

cv2.imshow('image', img)
cv2.waitKey()
cv2.destroyAllWindows()