from io import UnsupportedOperation
import cv2 as cv

from image import*
import os

# l = Image('../2713ML0142060011003969C00_DRCX.IMG')
# l = Image('../data/0126MR0007820040200791C00_DRCL.IMG')

dataPath = '../../data/'
outPath = '../../output/'

fovHor = 35  # degrees
fovVer = 6  # degrees
pxPerDeg = 100
canvasVerCenterDeg = -16
canvasHorCenterDeg = 233

# ignoreFiles = ['_DRLX', '_DRXX', '_DRCL']


def show_image(img, canvas):

        sizeVerPx = int(img.upperLimVert*pxPerDeg -
                        img.lowerLimVert*pxPerDeg)
        sizeHorPx = int(img.rightLimHor*pxPerDeg -
                        img.leftLimHor*pxPerDeg)
        # sizeVerPx = int(pxPerDeg*sizeVerDeg)
        # sizeHorPx = int(pxPerDeg*sizeHorDeg)

        print('Scaling to {}x{}'.format(sizeHorPx, sizeVerPx))

        scaledImg = cv.resize(
            img.img, (sizeHorPx, sizeVerPx))

        lowerLimVerPx = int(
            (img.lowerLimVert - canvasVerCenterDeg)*pxPerDeg)
        upperLimVerPx = lowerLimVerPx + sizeVerPx
        leftLimHorPx = int(
            (img.leftLimHor - canvasHorCenterDeg)*pxPerDeg)
        rightimHorPx = leftLimHorPx + sizeHorPx

        print('Placing image at [{}:{}][{}:{}]'.format(
            lowerLimVerPx, upperLimVerPx, leftLimHorPx, rightimHorPx))

        canvas[lowerLimVerPx:upperLimVerPx,
               leftLimHorPx:rightimHorPx] = scaledImg

        cv.imshow('canvas', canvas)
        cv.waitKey()

def get_out_path_base(img):
    fName = os.path.split(img.fName)[1]
    fName = os.path.splitext(fName)[0]
    outFilePath = os.path.join(outPath, fName)

    return outFilePath


def write_out_label(img):
    outLabelPath = get_out_path_base(img) + '.txt'
    with open(outLabelPath, 'w') as outLable: 
        outLable.write('{},{},{},{}'.format(img.rightLimHor, img.upperLimVert, img.leftLimHor, img.lowerLimVert))


def write_out_img(img):
    outImgPath = get_out_path_base(img) + '.bmp'
    cv.imwrite(outImgPath, img.img)


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

        show_image(imgObj, canvas)
        write_out_label(imgObj)
        write_out_img(imgObj)



        # TODO: use the angles parsed in `i` to place this image in a large cv mat
