import cv2
import numpy as np

# cv2 library is used to read and write images

# To read an image, we can use the imread method
img = cv2.imread('Class_26_05_12_2023/new_image.jpg')

# We can show the dimensions of the image using the ndim attribute
print(img.ndim)

# We can print the shape of the image using the shape attribute
print(img.shape)

# To display an image, we can use the imshow method
cv2.imshow('image', img)

# We can crop an image using the slicing operator
# The following will show a cropped image of size 100x100
cropped_img = img[0:100, 0:100]
cv2.imshow('cropped image', cropped_img)

# The waitKey method is used to wait for a key press
# cv2.waitKey(0)