import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('982990.jpg', cv2.IMREAD_GRAYSCALE) # Using Grayscale as it is much simplified, it's also efficient for image analysis.

""" More Options 

# IMREAD_COLOR - (1)
# IMREAD_GRAYSCALE - (0)
# IMREAD_UNCHANGED - (-1)

"""

# Showing/Displaying images in cv2.
cv2.imshow('image', img)
cv2.waitKey(0) 
cv2.destroyAllWindows()

# Showing/Displaying images in matplotlib.
# plt.imshow(img, cmap='gray', interpolation='bicubic')
# plt.plot([50, 100], [80, 100], 'c', linewidth=5)
# plt.show()

# To save an image.
cv2.imwrite('write_test.png', img)