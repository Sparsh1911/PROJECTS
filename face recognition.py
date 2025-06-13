# Modules 

import face_recognition
import cv2
import numpy as np

# Starting video capture
video_capture = cv2.VideoCapture(0)

#faces 
elonface = face_recognition.load_image_file("elon.jpg")
modiface = face_recognition.load_image_file("modi.jpg")

#Now creating the encodings of these base images using "face_encodings()" function
Elon_encoding=face_recognition.face_encodings(elonface)[0]
Modi_encoding=face_recognition.face_encodings(modiface)[0]

#Now creating two lists one to store face encodings and the other to store the names of these faces
Known_encodings=[Elon_encoding,Modi_encoding]
Known_faces=["Elon","Modi"]

#intitializing the variables 
face_locations = []
face_encodings = []
face_names = []
prtocess_this_frame = True #this program will process and analyze every other frame to save processing power

while True:
    ret.frame = video_capture.read()  # Capture frame-by-frame
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)  # Resize frame to 1/4 size for faster processing

#Here the code checks if the frame is to be processed or not, if process_this_frame = False then the frame will not be processed 

if prtocess_this_frame:
    #The location of the face of the user in front of the camera is taken
    face_locations = face_recognition.face_locations(small_frame)


#Creating the face encoding of the user and storing it in list 
    face_encodings = face_recognition.face_encodings(small_frame, face_locations)

    face_names = []
    for i in face_encodings:
        matches = face_recognition.compare_faces(Known_encodings, i)
        name = "Unknown"    
    if True in matches:
        first_match_index = matches.index(True)
        name = Known_faces[first_match_index]
    face_names.append(name)
    prtocess_this_frame = not prtocess_this_frame  # Toggle the processing flag

    for (top, right, bottom, left), name in zip(face_locations, face_names):
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 255, 0), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

        cv2.imshow('Video', frame)  # Display the resulting frame

        #To quit the program press 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
              break
    
    video_capture.release()  # Release the video capture object
    cv2.destroyAllWindows()  # Close all OpenCV windows

