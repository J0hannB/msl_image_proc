from io import UnsupportedOperation
import cv2 as cv

from image import*
import os

# l = Image('../2713ML0142060011003969C00_DRCX.IMG')
# l = Image('../data/0126MR0007820040200791C00_DRCL.IMG')

dataPath = '../data/'

fovHor = 35  # degrees
fovVer = 6  # degrees
pxPerDeg = 100
canvasVerCenterDeg = -16
canvasHorCenterDeg = 233

# ignoreFiles = ['_DRLX', '_DRXX', '_DRCL']

canvas = np.zeros((fovVer*pxPerDeg, fovHor*pxPerDeg, 3), np.uint8)

for file in os.listdir(dataPath):

    # ignore these file types until I figure out how to process them
    # or file.find('_DRCX') >= 0:
    if file.find('_DRLX') >= 0 or file.find('_DRXX') >= 0:
        continue

    if os.path.splitext(file)[1] == '.IMG' and file.find('_DRLX'):

        imgPath = os.path.join(dataPath, file)
        print('found image {}'.format(imgPath))
        labelPath = imgPath.replace('.IMG', '.LBL')

        if not os.path.exists(labelPath):
            print('Unable to find label for image! Skipping')
            continue

        imgObj = Image(imgPath)

        sizeVerPx = int(imgObj.upperLimVert*pxPerDeg -
                        imgObj.lowerLimVert*pxPerDeg)
        sizeHorPx = int(imgObj.rightLimHor*pxPerDeg -
                        imgObj.leftLimHor*pxPerDeg)
        # sizeVerPx = int(pxPerDeg*sizeVerDeg)
        # sizeHorPx = int(pxPerDeg*sizeHorDeg)

        print('Scaling to {}x{}'.format(sizeHorPx, sizeVerPx))

        scaledImg = cv.resize(
            imgObj.img, (sizeHorPx, sizeVerPx))

        lowerLimVerPx = int(
            (imgObj.lowerLimVert - canvasVerCenterDeg)*pxPerDeg)
        upperLimVerPx = lowerLimVerPx + sizeVerPx
        leftLimHorPx = int(
            (imgObj.leftLimHor - canvasHorCenterDeg)*pxPerDeg)
        rightimHorPx = leftLimHorPx + sizeHorPx

        print('Placing image at [{}:{}][{}:{}]'.format(
            lowerLimVerPx, upperLimVerPx, leftLimHorPx, rightimHorPx))

        canvas[lowerLimVerPx:upperLimVerPx,
               leftLimHorPx:rightimHorPx] = scaledImg

        cv.imshow('canvas', canvas)
        cv.waitKey()

        # TODO: use the angles parsed in `i` to place this image in a large cv mat
