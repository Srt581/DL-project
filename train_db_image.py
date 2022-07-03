# import the necessary packages
from imutils import paths
import face_recognition
import argparse
import pickle
import cv2
import os
base_dir = "./dataset"
model_name = "model_image.pickle"
try:
    os.remove(model_name)
except:
    pass
imagePaths = list(paths.list_images('dataset'))
print(imagePaths)
knownEncodings = []
knownNames = []
status = True
for file in imagePaths:
    print(file)
    rgb = cv2.imread(file)
    (s1, s2, s3) = rgb.shape
    # (top, right, bottom, left) = box
    box = [(0, s1, s2, 0)]
    (top, right, bottom, left) = box[0]
    roi_color = rgb[top:bottom, left:right]
    cv2.imshow("roi", roi_color)
    cv2.waitKey(100)
    encodings = face_recognition.face_encodings(rgb, box)[0]
    a = file.split("/")[1].split("_")[0]
    knownEncodings.append(encodings)
    knownNames.append(a)

print("[INFO] serializing encodings...")
data = {"encodings": knownEncodings, "names": knownNames}
f = open(model_name, "wb")
f.write(pickle.dumps(data))
f.close()