# import the necessary packages
from imutils import paths
import face_recognition
import argparse
import pickle
import cv2
import os
model_name = "model_video.pickle"
try:
    os.remove(model_name)
except:
    pass
cap = cv2.VideoCapture("./videos/video1.mp4")
print("[INFO] quantifying faces...")
imagePaths = list(paths.list_images('dataset'))
print(imagePaths)
knownEncodings = []
knownNames = []
status = True
while (status):
    ret, img = cap.read()
    if not ret:
        break
    rgb = img[:, :, ::-1]
    boxes = face_recognition.face_locations(rgb)
    print(boxes)
    for box in boxes:
        (top, right, bottom, left) = box
        roi_color = img[top:bottom, left:right]
        cv2.imshow("roi", roi_color)
        cv2.rectangle(img, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.imshow("img",img)
        cv2.waitKey(100)
        a1 = []
        a1.append(box)
        print(box)
        print(a1)
        encodings = face_recognition.face_encodings(rgb, a1)[0]
        a = input("enter the label: ")
        if a == 's':
            status = False
            break
        elif a == 'q':
            break
        knownEncodings.append(encodings)
        knownNames.append(a)

print("[INFO] serializing encodings...")
data = {"encodings": knownEncodings, "names": knownNames}
f = open(model_name, "wb")
f.write(pickle.dumps(data))
f.close()