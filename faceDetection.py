import numpy as np
import cv2

# Load in the face detector XML file
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Read in an image
image = cv2.imread('face1.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

#Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect the faces in the image
faces = face_cascade.detectMultiScale(gray, 1.3, 5)