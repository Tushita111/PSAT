import cv2
from PIL import Image, ImageTk, ImageDraw


def displayFrame(capture,frame):
    """
    Display the pose skeletton on top of the video frame
    
    Parameters
    ----------
    capture : cv2 frame from the video capture
    frame : one frame (x,y,likelyhood dataset) from the panda hdf pose file
    n_frame : number of the frame to display
    """
    
    # add joints to the frame
    xPoint = frame.loc['x']
    yPoint = frame.loc['y']
    img = Image.fromarray(capture)
    draw = ImageDraw.Draw(img)
    for i in range(20):
        x = xPoint[i]
        y = yPoint[i]
        node_label = xPoint.index[i]
        draw.ellipse(
            (x-3,y-3,x+3,y+3),fill='white'
        )
        draw.text(
            (x+3, y+3), node_label, stroke_width=12
        )
        
    # display frame
    img.show()