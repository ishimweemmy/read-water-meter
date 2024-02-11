import cv2 
import pytesseract 
import numpy as np

img = cv2.imread('meter.jpg') 

# Convert the image to gray scale 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 
# Use Gaussian blur to remove noise 
blur = cv2.GaussianBlur(gray, (5,5), 0) 
bin_img = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
 
# Perform dilation and erosion to remove some noise 
kernel = np.ones((1, 1), np.uint8) 
img = cv2.dilate(bin_img, kernel, iterations=1) 
img = cv2.erode(img, kernel, iterations=1) 

# Use pytesseract to convert the image data to text 
text = pytesseract.image_to_string(img) 

# Print the text 
print(text)