import pandas as pd
import numpy as np
import cv2
from PIL import Image


im = Image.open("../data/train/0.jpg")

# Reading an image in default mode
image = cv2.imread("../data/train/0.jpg")

# Window name in which image is displayed
window_name = 'Image'

x_0 = 180
x_1 = 598
y_0 = 889
y_1 = 1056

#shows the image# Start coordinate, here (5, 5)
# represents the top left corner of rectangle
start_point = (180, 889)

# Ending coordinate, here (220, 220)
# represents the bottom right corner of rectangle
end_point = (598, 1056)

# Blue color in BGR
color = (255, 0, 0)

# Line thickness of 2 px
thickness = 10

# Using cv2.rectangle() method
# Draw a rectangle with blue line borders of thickness of 2 px
image = cv2.rectangle(image, start_point, end_point, color, thickness)

# Displaying the image
cv2.imshow(window_name , image)
