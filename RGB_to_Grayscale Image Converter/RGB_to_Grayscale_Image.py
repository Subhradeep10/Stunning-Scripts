# importing libraries and modules
import cv2
import numpy as np
import urllib.request
from PIL import Image

# Change with the url of the image that needs to be gray scaled.
url = "https://raw.githubusercontent.com/HVbajoria/Automation-Scripts-Using-Python/main/RGB_to_Grayscale%20Image%20Converter/sample.jpg"

# Getting the image
url_response = urllib.request.urlopen(url)
img_array = np.array(bytearray(url_response.read()), dtype=np.uint8)
image = cv2.imdecode(img_array, -1)

# Display the original image
cv2.imshow('Original Image', image)
# Close the window on pressing '0'
cv2.waitKey(0)

# Using the cvtColor() function to grayscale the image
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Displaying the Grayscaled Image
cv2.imshow('Grayscale Image', gray_image)
# Close the window in pressing '0'
cv2.waitKey(0)
 
# Saving the gray scale image locally
status = cv2.imwrite('grayscaled_image.png',gray_image)

# Displaying download status
if status:
      print("Image Donwloaded Successfully")
else:
      print("Image Download Unsuccessfull")


cv2.destroyAllWindows()