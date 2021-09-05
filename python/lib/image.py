import cv2 as cv
import numpy as np

from label import*


class Image:

    def __init__(self, fName):

        lblName = fName.replace('.IMG', '.LBL')

        self.img = None
        self.rows = 0
        self.cols = 0
        self.label = Label(lblName)
        self.fName = fName

        self.read_image()
        self.parse_details()

    # read the image from the .IMG file based on the format described
    # in the label file

    def read_image(self):

        imgObj = self.label.objects['IMAGE']

        if imgObj is None:
            print('Error: No image object found in label!')
            return

        self.rows = int(imgObj['LINES'])
        self.cols = int(imgObj['LINE_SAMPLES'])

        print('Reading image of size {}x{}'.format(self.rows, self.cols))

        with open(self.fName, 'rb') as imgFile:

            channelCount = 3
            channels = []

            for c in range(0, channelCount):
                channel = np.zeros((self.rows, self.cols, 1), np.uint8)

                for i in range(0, self.rows):
                    for j in range(0, self.cols):

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

    def parse_details(self):

        instGroup = self.label.groups['INSTRUMENT_STATE_PARMS']

        if instGroup is None:
            print('Error: No instrument group found in label!')
            return

        self.verticalFov = float(instGroup['VERTICAL_FOV'])
        self.horizontalFov = float(instGroup['HORIZONTAL_FOV'])

        derivedParamsGroup = self.label.groups['DERIVED_IMAGE_PARMS']

        if derivedParamsGroup is None:
            print('Error: No derived image params group found in label!')
            return

        self.fixedInstAz = float(
            derivedParamsGroup['FIXED_INSTRUMENT_AZIMUTH'])
        self.fixedInstEl = float(
            derivedParamsGroup['FIXED_INSTRUMENT_ELEVATION'])

        # calculated params

        # units: degrees from horizontal plane [-90, 90]
        self.upperLimVert = self.fixedInstEl + self.verticalFov/2.0
        self.lowerLimVert = self.fixedInstEl - self.verticalFov/2.0

        # units: degrees from North [0, 360]
        self.rightLimHor = self.fixedInstAz + self.horizontalFov/2.0
        self.leftLimHor = self.fixedInstAz - self.horizontalFov/2.0

        print("Vertical limits [{},{}] deg".format(
            self.lowerLimVert, self.upperLimVert))
        print("Horizontal limits [{},{}] deg".format(
            self.leftLimHor, self.rightLimHor))
