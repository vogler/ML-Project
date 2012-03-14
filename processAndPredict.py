#from libs.pybrain.structure import FeedForwardNetwork
import os, sys
from scipy.io import loadmat

print "processing input images with octave and writing file octave/inputAndPredictedValues.mat"
os.system('run-processInput.bat')


input = loadmat('octave/inputAndPredictedValues.mat')

# input matrix of detected sudoku numbers
X = input['X']

# predicted values from octave
field = input['field']
pNN = input['pNN']
pSVM = input['pSVM']
pLR = input['pLR']

classes = zip(field, pNN)
print classes
for i,c in classes:
    print i/9, i%9, c