import cv2 as cv
from label import*

class Image:

    def __init__(self, fName):

        lblName = fName.replace('.IMG', '.LBL')

        self.label = Label(lblName)
