# System includes
import time
import os
import sys

# GIMP includes
from gimpfu import *

# Add project path to system path
# Must update PROJECT_PATH after cloning
PROJECT_PATH = 'C:\\Users\\jonat\\Documents\\PlanetaryScience\\MSL'
LIB_PATH = os.path.join(PROJECT_PATH, 'python\\lib')
sys.path.append(LIB_PATH)

# Local includes
from image import *

DATA_PATH = os.path.join(PROJECT_PATH, 'data')

def test_fn():

    for file in os.listdir(DATA_PATH):

        print(file)

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

    print('done')
    time.sleep(30)