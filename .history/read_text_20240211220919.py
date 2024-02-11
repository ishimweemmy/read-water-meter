import numpy as np
import pytesseract
import cv2

image = cv2.imread('ocr.jpg.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
sharpen_kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
sharpen = cv2.filter2D(gray, -1, sharpen_kernel)
thresh = cv2.threshold(sharpen, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

data = pytesseract.image_to_string(thresh, lang='eng', config='--psm 6')

numbers = ''.join(filter(str.isdigit, data))

print("Extracted Numbers:", numbers)