# -*- coding: utf-8 -*-
"""
Created on Fri Nov  25 08:42:49 2022

@author: Gsgwl
"""

import cv2
from PIL import Image, ImageTk, ImageDraw
import numpy as np
from tkinter import *
from tkinter import filedialog
from dlclive import benchmark, utils
import pandas as pd
import display.drawSkeleton as dS
import display.drawFrame as dF
'''import matplotlib.pyplot as plt'''                                                                                                                                                                                                                                                                                                                                                                                               

'''
modelpath = ''
filepath = ''


Frame from camera -> dlclive.processframe -> dlclive.init_inference -> dlclive.getpose

out :
Pose

-> 2d to 3d (voir avec Loann)

'''

def open_pose():
    global posepath
    posepath = filedialog.askopenfilename(title="Selectionner un fichier", filetypes=(("file_type","*.extension"),("all files","*.*")))

def open_video():
    global filepath
    filepath = filedialog.askopenfilename(title="Selectionner une video", filetypes=(("file_type","*.extension"),("all files","*.*")))

def open_mod():
    global modelpath
    modelpath = filedialog.askdirectory(title="Selectionner un modele")

def view_pose(n_frame):
    pose = pd.read_hdf(posepath)
    cap = cv2.VideoCapture(filepath)
    
    # Take the right frame from the video capture and the pose file
    cap.set(1,n_frame)
    ret, f = cap.read()
    frame = pose.loc[n_frame].swaplevel()
    
    dF.displayFrame(f,frame)

def analyse():
    benchmark(modelpath,filepath,display=False,pixels=45000,save_poses=True,save_video=True,n_frames=200,pcutoff=scale.get())
    
def norm(arr,mini,maxi):
    return (arr-mini)/(maxi-mini)
    
def view_model():
    pose = pd.read_hdf(posepath)
    frame = pose.loc[0].swaplevel()
    
    xPoint = frame.loc['x']
    yPoint = frame.loc['y']
    
    # normalize arrays while keeping shape
    mini = np.minimum(np.min(xPoint),np.min(yPoint))
    maxi = np.maximum(np.max(xPoint),np.max(yPoint))
    xPointN = norm(xPoint,mini,maxi)
    yPointN = norm(yPoint,mini,maxi)
    label = xPoint.index
    
    dS.displaySkeleton(xPointN,yPointN,np.zeros(20),label)

def launch():
    view_model()
    
    
window=Tk()

scale=DoubleVar()

Label(window, text="Selectionner", font='Arial 16 bold').pack(pady=15)

button_video = Button(window, text="Choisir video", command=open_video)
button_video.pack()
button_modele = Button(window, text="Choisir modele", command=open_mod)
button_modele.pack()
button_launch = Button(window, text="Analyse video", command=launch)
button_launch.pack()
button_pose = Button(window, text="Choisir poses", command=open_pose)
button_pose.pack()
entry_frame = Entry(window,text='Frame a visualiser')
entry_frame.insert(0,'0')
entry_frame.pack()
button_view = Button(window, text="Visualiser le squelette", command=lambda:view_pose(int(entry_frame.get())))
button_view.pack()

Scale(
    master=window,
    from_=0,
    to=1,
    resolution=0.05,
    orient=HORIZONTAL,
    variable=scale
).pack(side=BOTTOM)

window.mainloop()