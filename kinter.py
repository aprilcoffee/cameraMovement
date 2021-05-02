import cv2
import time,sys
from PIL import Image, ImageTk
import math
import screeninfo
import numpy as np
#from tkinter import Tk, Label
import tkinter as tk
#from tkinter import ttk
root = tk.Tk()

# Hide the root window drag bar and close button
#root.overrideredirect(True)
# Make the root window always on top
root.wm_attributes("-topmost", True)
root.wm_attributes('-fullscreen','true')
# Turn off the window shadow
root.wm_attributes("-transparent", True)
# Set the root window background color to a transparent color
root.config(bg='systemTransparent')

root.geometry("+300+300")


#canvas = Canvas(root,width=500,height=800)
#canvas.pack()



speed = 0.3
h = 300
w = 400
resize_w = 720
resize_h = 480
which_cam = 1

#screen = screeninfo.get_monitors()[0]
#s_width, s_height = screen.width, screen.height

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
#cv2.namedWindow(window_name,flags=cv2.WINDOW_GUI_NORMAL)
#cv2.moveWindow(window_name, int(screen.x-1), int(screen.y-1))
#cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)

print(returnCameraIndexes())
cap = cv2.VideoCapture(which_cam)
x = 0
y = 0
index = 0

lmain = tk.Label(root)
lmain.config(bg='systemTransparent')
lmain.pack()

def show_frame():
    global x,y,index
    _, frame = cap.read()
    index += speed
    height, width, channels = frame.shape
    y = int(height/2)
    x = int(abs((width-w)*math.sin(math.radians(index))))
    crop = frame[y:y+h, x:x+w]

    frame = cv2.flip(crop, 1)
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, show_frame)


show_frame()
root.mainloop()

print('direct out')
cap.release()
cv2.destroyAllWindows()
