import cv2 as cv
import numpy as np

from label import*

class Image:

    def __init__(self, fName):

        lblName = fName.replace('.IMG', '.LBL')

        self.label = Label(lblName)
        self.fName = fName

        self.read_image()




    def read_image(self):

        imgObj = self.label.objects['IMAGE']

        if imgObj is None:

            print('Error: No image object found in label!')
            return

        rows = int(imgObj['LINES'])
        cols = int(imgObj['LINE_SAMPLES'])

        print('Reading image of size {}x{}'.format(rows, cols))

        img = np.zeros((rows,cols,3), np.uint8)

        with open(self.fName, 'rb') as imgFile:

            for i in range(0, rows):
                for j in range(0, cols):

                    b = imgFile.read(1)

                    img[i][j] = ord(b)

        cv.imshow('img', img)
        cv.waitKey()