import cv2
import time,sys
from PIL import Image, ImageTk
import math


speed = 0.3
h = 300
w = 400
which_cam = 1

def returnCameraIndexes():
    # checks the first 10 indexes.
    index = 0
    arr = []
    i = 10
    while i > 0:
        cap = cv2.VideoCapture(index)
        if cap.read()[0]:
            arr.append(index)
            cap.release()
        index += 1
        i -= 1
    return arr

print(returnCameraIndexes())
cap = cv2.VideoCapture(which_cam)
x = 0
y = 0
index = 0
while(cap.isOpened()):
    ret,frame = cap.read()
    index += speed
    height, width, channels = frame.shape
    y = int(height/2)
    x = int(abs((width-w)*math.sin(math.radians(index))))
    crop = frame[y:y+h, x:x+w]
    cv2.imshow('Image', crop)

    key = cv2.waitKey(1)
    if key==32:
        new = False
    if key==27 or key==ord('q'):
        break

print('direct out')
cap.release()
cv2.destroyAllWindows()
