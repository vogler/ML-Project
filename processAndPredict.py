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

def section(s):
    print 
    print '-'*6+' '+s+' '+'-'*6

def unique(seq):
    seen = set()
    seen_add = seen.add
    return [ x for x in seq if x not in seen and not seen_add(x)]

field_param = ''
rows = [[] for i in range(9)]
cols = [[] for i in range(9)]
predicted_values = [0 for i in range(9*9)]
for i,c in zip(field, pSVM):
    i, c = int(i), int(c)
    predicted_values[i-1] = c
    row = int((i-1)/9)
    col = int((i-1)%9)
    print i, row, col, c
    field_param += ' '+str(row)+str(col)+str(c)
    rows[row].append(c)
    cols[col].append(c)

# accuracy
section('Accuracy')
# filter(lambda a: a 0= 0, predicted_values)
solution = [
3,0,0, 2,4,0, 0,6,0,
0,4,0, 0,0,0, 0,5,3,
1,8,9, 6,3,5, 4,0,0,
0,0,0, 0,8,0, 2,0,0,
0,0,7, 4,9,6, 8,0,1,
8,9,3, 1,5,0, 6,0,4,
0,0,1, 9,2,0, 5,0,0,
2,0,0, 3,0,0, 7,4,0,
9,6,0, 5,0,0, 3,0,2]
correct = [a for (a,b) in zip(solution,predicted_values) if a==b]
failed  = [(i+1,a,b) for (i,a,b) in zip(range(9*9), solution,predicted_values) if a!=b]
print 'Correct: ', len(correct), 'Failed: ', len(failed)
print failed
print 'Accuracy: ', len(correct)/(9.*9)


section('Valid Sudoku?')
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

section('Solver')
os.system('java -cp . Sudoku'+field_param)