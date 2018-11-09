# This will be a simple implementation of a cell counting algorithm.
# Steps involved include:
# 1. Importing a .tif stack (3-D volume)
# 2. Loading the .tif stack into a numpy array
# 3. Importing landmarks - .marker files, typically obtained from the Vaa3D software
# 4. Checking each landmark to ensure it corresponds to a cell
# 5. Extracting feature vectors from the landmarks **
# 6. Training the model - SVM, sklearn?
# 7. Test on the remaining points - k-fold testing

import numpy as np
import os
import tifffile as tf
from numpy import empty
from numpy import hstack
# from PIL import Image

# * Doesn't check if directory exists *
# def load_tiff():
tiffAList = []
nameList = []
fileCount = 0

tiffDirectory = input("Provide the address of the directory containing the tiff files to open >> ")
print(tiffDirectory)

for filename in os.listdir(tiffDirectory):
    if filename.endswith(".tif") or filename.endswith(".tiff"):
        #
        filepath = tiffDirectory + "/" + filename
        readIm = tf.imread(filepath)
        tiffAList.append(readIm)
        nameList.append(filename)
    else:
        print("File", filename, "does not have the .tif or .tiff file extension.")
nameList.sort()
for name in nameList:
    print(name)
