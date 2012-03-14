#from libs.pybrain.structure import FeedForwardNetwork
import os, sys
from scipy.io import loadmat

print "processing input images with octave and writing file nn/input.mat"
os.system('run-processInput.bat')


input = loadmat('nn/inputAndPredictedValues.mat')

# input matrix of detected sudoku numbers
X = input['X']

# predicted values from octave
pNN = input['pNN']
pSVM = input['pSVM']
pLR = input['pLR']
