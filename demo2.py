# import the necessary packages
from imutils.video import VideoStream
from imutils.video import FPS
import face_recognition
import argparse
import imutils
import pickle
import time
import cv2
import numpy as np

# model_name = "model_video.pickle"
model_name = "model_image.pickle"
data = pickle.loads(open(model_name, "rb").read())
known_face_encodings = data['encodings']
known_face_names= data['names']
frame_count = 30
thresh = 15
# Grab a single frame of video
# frame = cv2.imread("kang33.jpg")

# Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
# rgb_frame = frame[:, :, ::-1]
cap = cv2.VideoCapture('./videos/video3.mp4')
i = 0
identified_name = []
det = [0,0]
while (cap.isOpened()):
    ret, frame = cap.read()
    rgb_frame = frame[:, :, ::-1]
    print("{} frame".format(i))
    if i<frame_count:
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
        cnt = 0
        # Loop through each face in this frame of video
        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            print(matches)
            name = "Unknown"
            # Or instead, use the known face with the smallest distance to the new face
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            max_match = np.min(face_distances)
            print(max_match)
            best_match_index = np.argmin(face_distances)
            if max_match < 0.4:
                print("xxxxxxxx",best_match_index)
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]
                    identified_name.append(name)
                    print(name)
                    det[int(name)-1] = det[int(name)-1] + 1

            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
            cnt=cnt+1
    else:
        break
    print(det)
    i=i+1
    cv2.imshow('Video', frame)
    cv2.waitKey(100)

sent = "Person detected: "
if sum(det)>0:
    for dd in range(len(det)):
        if det[dd] > thresh:
            sent = sent + "{}, ".format(dd+1)
else:
    sent = sent + "No One"

print(sent)

