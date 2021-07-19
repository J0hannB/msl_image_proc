import cv2 as cv
import numpy as np

from label import*

class Image:

    def __init__(self, fName):

        lblName = fName.replace('.IMG', '.LBL')

        self.label = Label(lblName)
        self.fName = fName

        self.read_image()


    # read the image from the .IMG file based on the format described
    # in the label file
    def read_image(self):

        imgObj = self.label.objects['IMAGE']

        if imgObj is None:

            print('Error: No image object found in label!')
            return

        rows = int(imgObj['LINES'])
        cols = int(imgObj['LINE_SAMPLES'])

        print('Reading image of size {}x{}'.format(rows, cols))


        with open(self.fName, 'rb') as imgFile:

            channelCount = 3
            channels = []

            for c in range(0, channelCount):

                channel = np.zeros((rows,cols,1), np.uint8)

                for i in range(0, rows):
                    for j in range(0, cols):

                        b = imgFile.read(1)

                        channel[i][j] = ord(b)

                channels.append(channel)

        print('channels: {}'.format(len(channels)))

        r = channels[0]
        g = channels[1]
        b = channels[2]

        self.img = cv.merge((b, g, r))

        cv.imshow('img', self.img)
        # cv.imshow('r', r)
        # cv.imshow('g', g)
        # cv.imshow('b', b)
        cv.waitKey()
