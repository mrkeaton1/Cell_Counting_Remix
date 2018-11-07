# This will be a simple implementation of a cell counting algorithm.
# Steps involved include:
# 1. Importing a .tif stack (3-D volume)
# 2. Loading the .tif stack into a numpy array
# 3. Importing landmarks - .marker files, typically obtained from the Vaa3D software
# 4. Checking each landmark to ensure it corresponds to a cell
# 5. Extracating feature vectors from the landmarks **
# 6. Training the model - SVM, sklearn?
# 7. Test on the remaining points - k-fold testing
from PIL import Image

# def load_tiff():

newIm = Image.open('New Stack/3-weeks post-siso EdU every 6 hours PINK 6_z000.tif')
newIm.show()
