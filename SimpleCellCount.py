# This will be a simple implementation of a cell counting algorithm.
# Steps involved include:
# 1. Importing a .tif stack (3-D volume)
# 2. Loading the .tif stack into a numpy array
# 3. Importing landmarks - .marker files, typically obtained from the Vaa3D software =+=
# 4. Checking each landmark to ensure it corresponds to a cell
# 5. Extracting feature vectors from the landmarks **
# 6. Training the model - SVM, sklearn?
# 7. Test on the remaining points - k-fold testing

import numpy as np
import os
import tifffile as tf
import sys
from numpy import empty
from numpy import hstack
# from PIL import Image
import re
import glob
from natsort import natsorted

tiffAList = [] # List containing each tif image in a numpy array
markLList = [] # List of each marker

def naturalSort(l):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
    return sorted(l, key = alphanum_key)

def findTiffsInPath(tiffDirectory):
	if not os.path.isdir(tiffDirectory):
		print("can't find directory")
		return

	#instead of using input, use sys.argv to pass parameters into a script via command line
	print("Loading all .tif files from " + tiffDirectory)

	nameList = glob.glob(tiffDirectory + "*.tif*")
	naturalSort(nameList)
	for name in nameList:
		print(name)

	return nameList

def loadTiffs(tiffDirectory, tiffList):
        for fileName in tiffList:
            readIm = tf.imread(fileName)
            tiffAList.append(readIm)

def loadMarker(markerFile):
    if not os.path.isfile(markerFile):
        print("can't find .marker file")
        return
    print("Loading .marker file")
    markers = [line.rstrip('\n') for line in open(markerFile)]
    for marker in markers[1:]: # Skip 1st row containing name of volume
        print(marker)
        markSplit = marker.split(',')
        markLList.append(markSplit[:5]) # Only keeps x, y, z, radius, and shape (Ignores name and comment)
    print("Resulting list:")
    print(markLList)
    return

# Commented out because it was giving back "IndentationError: unindent does not match any outer indentation level"
# if __name__ == '__main__':
# 	fileToSearch = sys.argv[1]
# 	tiffNamesList = findTiffsInPath(fileToSearch);
#     loadTiffs(fileToSearch, tiffNamesList)

if len(sys.argv) != 3:
    print("Incorrect number of arguments, format should be as follows:\nSimpleCellCount.py <tiff_files_directory> <marker_file_pathway>")
else:
    fileToSearch = sys.argv[1]
    markerFileName = sys.argv[2]
    loadTiffs(fileToSearch, findTiffsInPath(fileToSearch))
    loadMarker(markerFileName)
