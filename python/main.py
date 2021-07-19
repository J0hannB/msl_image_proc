import cv2 as cv

from image import*
import os

# l = Image('../2713ML0142060011003969C00_DRCX.IMG')
# l = Image('../data/0126MR0007820040200791C00_DRCL.IMG')

dataPath = '../data/'

for file in os.listdir(dataPath):

    # ignore these file types until I figure out how to process them
    if file.find('_DRLX') >= 0 or file.find('_DRXX') >= 0:
        continue

    if os.path.splitext(file)[1] == '.IMG' and file.find('_DRLX'):

        imgPath = os.path.join(dataPath, file)
        print('found image {}'.format(imgPath))
        labelPath = imgPath.replace('.IMG', '.LBL')

        if not os.path.exists(labelPath):
            print('Unable to find label for image! Skipping')
            continue


        i = Image(imgPath)

        # TODO: use the angles parsed in `i` to place this image in a large cv mat
