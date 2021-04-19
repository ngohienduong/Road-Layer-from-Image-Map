import numpy as np
import cv2
#Import image
image = cv2.imread('vietnam-transport.jpg')

#Edit this based on find hsv range.py
hsv_low =[0, 70, 178]
hsv_high=[5, 255, 255]

# Getting boundary layer in jpg
def rc2h(x):
  d = cv2.cvtColor(x, cv2.COLOR_RGB2HSV)
  return d
mask = cv2.inRange(rc2h(image), np.array([0, 70, 178]), np.array([5, 255, 255]))

#Edit path
cv2.imwrite('', boundary)