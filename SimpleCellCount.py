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
import sys
from numpy import empty
from numpy import hstack
# from PIL import Image
import re
import glob

def naturalSort(l): 
    convert = lambda text: int(text) if text.isdigit() else text.lower() 
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(l, key = alphanum_key)

# * Doesn't check if directory exists *
def findTiffsInPath(tiffDirectory):
	#tiffAList = []
	#nameList = []
	#fileCount = 0
	if not os.path.isdir(tiffDirectory):
		print("can't find directory")
		return

	#instead of using input, use sys.argv to pass parameters into a script via command line
	#tiffDirectory = input("Provide the address of the directory containing the tiff files to open >> ")
	print("Loading all .tif files from " + tiffDirectory)

	#for filename in os.listdir(tiffDirectory):
	#	if filename.endswith(".tif") or filename.endswith(".tiff"):
	#		#
	#		filepath = tiffDirectory + "/" + filename
	#		readIm = tf.imread(filepath)
	#		tiffAList.append(readIm)
	#		nameList.append(filename)
	#	else:
	#	print("File", filename, "does not have the .tif or .tiff file extension.")
	
	nameList = glob.glob(tiffDirectory + "*.tif*")
	naturalSort(nameList)
	for name in nameList:
		print(name)

	return nameList
		
if __name__ == '__main__':
	fileToSearch = sys.argv[1]
	tiffNamesList = findTiffsInPath(fileToSearch);