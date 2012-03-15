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


def unique(seq):
    seen = set()
    seen_add = seen.add
    return [ x for x in seq if x not in seen and not seen_add(x)]

field_param = ''
rows = [[] for i in range(9)]
cols = [[] for i in range(9)]
for i,c in zip(field, pNN):
    i, c = int(i), int(c)
    row = int((i-1)/9)
    col = int((i-1)%9)
    print i, row, col, c
    field_param += ' '+str(row)+str(col)+str(c)
    rows[row].append(c)
    cols[col].append(c)

error = False
for row, col in zip(rows, cols):
    if row != unique(row) or col != unique(col):
        print 'ERROR: duplicate number in row or column (1-9 allowed at most once)'
        print 'row: ', row
        print 'col: ', col
        error = True
if error:
        print 'WARNING: Solver will run forever (just used to display Sudoku field)'
        # exit()
os.system('java -cp . Sudoku'+field_param)