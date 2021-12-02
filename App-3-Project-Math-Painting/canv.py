import numpy as np
from PIL import Image


class Canvas:
    """
    creates the image containing the shapes
    """
    def __init__(self, width, height, color):
        self.color = color
        self.width = width
        self.height = height

        #create a 3d array of zeros
        self.data = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        #change the color of the array into user given values for color
        self.data[:] = self.color

    def make(self, imagepath):

        img = Image.fromarray(self.data, 'RGB')
        img.save(imagepath)