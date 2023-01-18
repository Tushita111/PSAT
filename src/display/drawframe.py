import cv2
from PIL import Image, ImageTk, ImageDraw


def displayFrame(capture,pose,n_frame):
    """
    Display the pose skeletton on top of the video frame
    
    Parameters
    ----------
    capture : cv2 video capture
    pose : panda hdf pose file
    n_frame : number of the frame to display
    """
    capture.set(1,n_frame)
    ret, f = cap.read()
    img = Image.fromarray(f)
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
    img.show()