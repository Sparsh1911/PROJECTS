# Modules 

import face_recognition
import cv2
import numpy as np

# Starting video capture
video_capture = cv2.VideoCapture(0)

#faces 
elonface = face_recognition.load_image_file("elon.jpg")
modiface = face_recognition.load_image_file("modi.jpg")
