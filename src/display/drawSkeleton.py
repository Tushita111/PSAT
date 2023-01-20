# Import libraries
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D




def test():
    # Change the Size of Graph using
    # Figsize
    fig = plt.figure(figsize=(10, 10))

    # Generating a 3D sine wave
    ax = plt.axes(projection='3d')

    # Creating array points using
    # numpy
    x = np.arange(0, 20, 0.1)
    y = np.sin(x)
    z = y*np.sin(x)
    c = x + y

    # To create a scatter graph
    ax.scatter(x, y, z, c=c)

    # turn off/on axis
    plt.axis('off')

    # show the graph
    plt.show()


def displaySkeleton(x,y,z,label=None):
    """
    display a 3D view from a 3d points cloud
    Parameters
    -----------
    x,y,z : array of points on each 3d axes
    """
    fig = plt.figure(figsize=(10, 10))
    ax = plt.axes(projection='3d')
    c = x + y
    ax.scatter(x, y, z, c=c)
    
    if(label is not None):
        for i in range(20):
            ax.text(x[i] ,y[i], z[i], label[i])
        
    plt.show()