import cv2
import time,sys
from PIL import Image, ImageTk
import math
import screeninfo


speed = 0.3
h = 300
w = 400
resize_w = 720
resize_h = 480
which_cam = 1

screen = screeninfo.get_monitors()[0]
s_width, s_height = screen.width, screen.height

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

window_name = 'projector'
cv2.namedWindow(window_name,flags=cv2.WINDOW_GUI_NORMAL)
#cv2.moveWindow(window_name, int(screen.x-1), int(screen.y-1))
#cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)

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

    # Show image and move it to center location
    image = cv2.resize(crop,(resize_w, resize_h))

    cv2.moveWindow(window_name, int((s_width/2)-(resize_w/2)), int((s_height/2)-(resize_h/2)))
    cv2.imshow(window_name,image)

    key = cv2.waitKey(1)
    if key==32:
        new = False
    if key==27 or key==ord('q'):
        break

print('direct out')
cap.release()
cv2.destroyAllWindows()
