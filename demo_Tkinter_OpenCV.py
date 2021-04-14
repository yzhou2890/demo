



''' demo of using Tkinter for showing webcam video with GUI functions  '''

''' use <c> to toggle cropping mode via left mouse button  '''

''' use <z> to zoom out  '''
''' use <Z> to zoom in '''




import numpy as np
import sys
import Tkinter as tk
import cv2
from PIL import Image, ImageTk



class Video():

    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.width = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        self.viewScale = True
        self.bCrop = True
        self.bZoom = True
        self.CropRect=[1,1,self.width,self.height]
        
        self.root = tk.Tk()
        self.root.bind('<Escape>', lambda e: self.root.quit())
        self.root.bind('<Key>',self.key)
        self.root.bind('<ButtonPress-1>',self.LeftButtonDown)
        self.root.bind('<ButtonRelease-1>',self.LeftButtonUp)
        self.lmain = tk.Label(self.root)
        self.lmain.pack()
    
        self.update_frame()
        self.show_frame()
        self.root.title('Video with GUI function: <Z> - zoom in, <z>-zoom out,<c> to toggle crop mode')
        self.root.mainloop()
    

    def update_frame(self):
        _, frame = self.cap.read()
        self.frame = cv2.flip(frame, 1)
        self.cv2image = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
        self.img = Image.fromarray(self.cv2image)
    
    def update_view(self):
        if self.bCrop:
            self.update_view_via_cropping()
    
    def show_frame(self):
        self.update_frame()
        self.imgtk = ImageTk.PhotoImage(image= self.img)
        self.lmain.imgtk = self.imgtk
        self.lmain.configure(image= self.imgtk)
        self.lmain.after(10, self.show_frame)

    def update_view_via_cropping(self):
        
        self.img=self.img.crop(self.CropRect)

    def update_view_via_scale(self,f):
        self.viewScale = f
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, int(float(self.width)*f))
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, int(float(self.height)*f))

        print "scaling down"

    def update_view_via_width_height(self, w, h):

        c = max( float(w)/self.width, float(h)/self.height )
    
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, int(float(self.width)*c))
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, int(float(self.height)*c))

        print self.width, self.height, self.width*c, self.height*c

    def toggle_crop_mode(self):
        self.bCrop = not self.bCrop
        print "Crop mode: " , self.bCrop

    def key(self, event):
        if (event.keysym == 'z'):
            self.update_view_via_scale(0.9*self.viewScale)
        elif (event.keysym == 'Z'):
            self.update_view_via_scale(1.1*self.viewScale)
        elif (event.keysym == 'c'):
            self.toggle_crop_mode()

    def LeftButtonDown(self,event):
        if self.bCrop:
            self.CropRect[0:] = event.x, event.y
            print self.CropRect

    def LeftButtonUp(self,event):
        if self.bCrop:
            self.CropRect[2:] = event.x - self.CropRect[0], event.y - self.CropRect[1]
            print self.CropRect
            img = self.frame[ self.CropRect[1]:self.CropRect[1]+self.CropRect[3],
                                 self.CropRect[0]:self.CropRect[0]+self.CropRect[2] ]
            try:
                cv2.imshow('cropped image', img)
            except:
                print "crop failed: select top-left first, then bottom-right"
                self.CropRect = [1, 1, self.width,self.height]
            else:
                cv2.waitKey(0)
                cv2.destroyAllWindows()







class Frame():
    
    def __init__(self):
        self.cv2img = cv2.imread('fruits.jpg',1)
        self.img    = Image.fromarray(self.cv2img)
        
        self.root = tk.Tk()
        self.root.bind('<Escape>', lambda e: self.root.quit())
        self.root.bind('<Key>',self.key)
        self.root.bind('<ButtonPress-1>',self.LeftButtonDown)
        self.root.bind('<ButtonRelease-1>',self.LeftButtonUp)
        self.lmain = tk.Label(self.root)
        self.lmain.pack()
        
        self.imgtk = ImageTk.PhotoImage(image= self.img)
        self.lmain.imgtk = self.imgtk
        self.lmain.configure(image= self.imgtk)
        self.lmain.after(10, self.show_frame)

        
        
        self.root.title('Video with GUI function: <Z> - zoom in, <z>-zoom out,<c> to toggle crop mode')
        self.root.mainloop()
    
    def show_frame(self):
        pass
    
    def key(self, event):
        if (event.keysym == 'z'):
            self.update_view_via_scale(0.9*self.viewScale)
        elif (event.keysym == 'Z'):
            self.update_view_via_scale(1.1*self.viewScale)
        elif (event.keysym == 'c'):
            self.toggle_crop_mode()

    def LeftButtonDown(self,event):
        if self.bCrop:
            print 'Left button Down'

    def LeftButtonUp(self,event):
        if self.bCrop:
            print 'left button up'

g1 = Frame()





