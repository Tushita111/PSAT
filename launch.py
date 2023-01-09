# -*- coding: utf-8 -*-
"""
Created on Fri Nov  25 08:42:49 2022

@author: Gsgwl
"""

import cv2
import numpy as np
from tkinter import *
from tkinter import filedialog
from dlclive import benchmark

'''
modelpath = ''
filepath = ''


Frame from camera -> dlclive.processframe -> dlclive.init_inference -> dlclive.getpose

out :
Pose

-> 2d to 3d (voir avec Loann)

'''


def open_video():
    global filepath
    filepath = filedialog.askopenfilename(title="Selectionner une video", filetypes=(("file_type","*.extension"),("all files","*.*")))
   
def open_mod():
    global modelpath
    modelpath = filedialog.askdirectory(title="Selectionner un modele")
      
def launch():
    benchmark(modelpath,filepath,display=True,pixels=45000,pcutoff=scale.get())
  
window=Tk()

scale=DoubleVar()

Label(window, text="Selectionner", font='Arial 16 bold').pack(pady=15)

button_video = Button(window, text="Choisir video", command=open_video)
button_video.pack()
button_modele = Button(window, text="Choisir modele", command=open_mod)
button_modele.pack()
button_launch = Button(window, text="Lancer", command=launch)
button_launch.pack()

Scale(
    master=window,
    from_=0,
    to=1,
    resolution=0.05,
    orient=HORIZONTAL,
    variable=scale
).pack(side=BOTTOM)

window.mainloop()