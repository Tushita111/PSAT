# -*- coding: utf-8 -*-
"""
Created on Fri Nov  25 08:42:49 2022

@author: Gsgwl
"""

import cv2
import numpy as np
from tkinter import *
from tkinter import filedialog
from dlclive import benchmark, utils
import pandas as pd
'''import matplotlib.pyplot as plt'''
from PIL import Image, ImageTk, ImageDraw

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

def launch():
    benchmark(modelpath,filepath,display=True,pixels=45000,save_poses=True,n_frames=200,pcutoff=scale.get())

def view_pose(n_frame):
    
    pose = pd.read_hdf(posepath)
    frame = pose.loc[n_frame].swaplevel()
    xPoint = frame.loc['x']
    yPoint = frame.loc['y']
    
    
    cap = cv2.VideoCapture(filepath)
    cap.set(1,n_frame)
    ret, f = cap.read()
    '''
    im_size = (cap.get(cv2.CAP_PROP_FRAME_WIDTH), cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    resize = np.sqrt(45000 / (im_size[0] * im_size[1]))
    im_size = (int(im_size[0] * resize), int(im_size[1] * resize))
    f = utils.resize_frame(f, resize)
    '''
    img = Image.fromarray(f)
    draw = ImageDraw.Draw(img)
    for i in range(20):
        x = xPoint[i]
        y = yPoint[i]
        node_label = xPoint.index[i]
        draw.ellipse(
            [x-1,x+1,y-1,y+1]
        )
        draw.text(
            [x, y], node_label, stroke_width=12
        )
    
    img.show()
    '''
    plt.scatter(xPoint,yPoint)
    for i in range(20):
        plt.annotate(xPoint.index[i], (xPoint[i], yPoint[i]), fontsize=12)
    plt.show()
    '''

    
    
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