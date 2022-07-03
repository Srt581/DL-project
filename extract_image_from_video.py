import cv2
import os
import face_recognition
base_dir = "./dataset"
framerate = 30
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture("./videos/video2.mp4")
total_file = [int(file.split("_")[1].split(".")[0])  for file in os.listdir(base_dir)]
print(total_file)
if len(total_file)>0:
    cnt = max(total_file) + 1
else:
    cnt = 1
# cnt = 1
status = True
frame_count = 0
while (status):
    ret, img = cap.read()
    if not ret:
        break
    frame_count +=1
    print(frame_count)
    if frame_count % framerate == 0:
        print("xxxxxxxxxxxxxxxxxxxxx")
        rgb = img[:, :, ::-1]
        boxes = face_recognition.face_locations(rgb)
        print(boxes)
        for box in boxes:
            (top, right, bottom, left) = box
            roi_color = img[top:bottom, left:right]
            cv2.imshow("roi", roi_color)
            cv2.waitKey(100)
            a = input("enter the label: ")
            if a == 's':
                status = False
                break
            elif a == 'q':
                break
            filename = "{}/{}_{}.png".format(base_dir,a,cnt)
            cv2.imwrite(filename,roi_color)
            cnt+=1
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

print("total frame: ",frame_count)
cap.release()
cv2.destroyAllWindows()
