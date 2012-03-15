import os, sys
from nnPredict import predict
from scipy.io import loadmat

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

def section(s):
    print 
    print 
    print '-'*6+' '+s+' '+'-'*6

def unique(seq):
    seen = set()
    seen_add = seen.add
    return [ x for x in seq if x not in seen and not seen_add(x)]

def checkAccuracy(pred, printFailed=False):
    predicted_values = [0 for i in range(9*9)]
    for i,c in zip(field, pred):
        predicted_values[i-1] = c
    correct         = [a for (a,b) in zip(solution,predicted_values) if a==b]
    correctNumbers  = len([x for x in correct if x!=0])
    failed          = [(i+1,a,b) for (i,a,b) in zip(range(9*9), solution,predicted_values) if a!=b]
    print 'Correct: ', len(correct), 'Failed numbers: ', 42-correctNumbers
    if printFailed: print failed
    print 'Accuracy: ', len(correct)/(9.*9)
    print 'Accuracy for numbers: ', correctNumbers, '/', 42, '->', correctNumbers/42.

def prediction(name, value=[]):
    pred = value if len(value) else [int(x[0]) for x in input[name]]
    if -1 in pred: pred = []
    print name, pred
    if len(pred): checkAccuracy(pred)
    print
    return pred

def main():
    global input, field
    print "processing input images with octave and writing file octave/inputAndPredictedValues.mat"
    os.system('run-processInput.bat')

    input = loadmat('octave/inputAndPredictedValues.mat')

    # input matrix of detected sudoku numbers
    X = input['X']
    # predicted values from octave
    field = [int(x[0]) for x in input['field']]
    section('Predictions')
    pNN      = prediction('pNN')
    pSVM     = prediction('pSVM')
    pLR      = prediction('pLR')
    pPyBrain = prediction('pPyBrain', predict())

    predictMethod = 'pNN'
    print '-> Using ', predictMethod
    p = eval(predictMethod)

    # creating list of params for solver
    field_param = ''
    rows = [[] for i in range(9)]
    cols = [[] for i in range(9)]

    for i,c in zip(field, p):
        row = int((i-1)/9)
        col = int((i-1)%9)
        # print i, row, col, c
        field_param += ' '+str(row)+str(col)+str(c)
        rows[row].append(c) # used for error checking
        cols[col].append(c)

    # accuracy
    section('Accuracy')
    checkAccuracy(p, True)

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

if __name__ == '__main__':
    main()