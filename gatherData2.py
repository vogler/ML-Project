import os, sys, glob, shutil
from processAndPredict import solution
from gatherData import number_input
from gatherData import getNewFilename

ext    = '.png'
input  = 'input/*'+ext
output = 'data2/'
cache  = output+'cache.mat'
cv_img = 'cv/sudoku.png'


def inputSolution():
    return solution
    sol = []
    for i in range(1, 9*9+1):
        sol.append(number_input(str(i)+'. field: '))
    print 'Entered solution:', sol
    return sol

def classify(sol):
    for f in glob.glob(input):
        i = int(os.path.basename(f).replace(ext, ''))
        c = sol[i-1]
        ff = getNewFilename(c)
        print 'move', f, ff
        shutil.move(f, ff)

def main():
    print "This program will train the same Sudoku multiple times. First you will enter the solution like so:"
    print solution
    print "Then you just have to capture the Sudoku as many times as you like."
    print "Hit 'x' to quit."
    if not os.path.exists(output):
        [os.makedirs(output+str(i)) for i in range(0,10)]
    sol = inputSolution()
    run = True
    while run:
        # delete existing capture so that the same samples aren't added twice
        if os.path.exists(cv_img):
            os.remove(cv_img)
        else:
            if raw_input("No input image found. Press 'x' to quit, anything else to continue and capture one.")=='x': break
        # fresh image from capture
        os.system('run-cv.bat')
        # split image and save in input
        os.system('python splitImage.py')
        # delete cache before any new samples are added
        if os.path.exists(cache): os.remove(cache)
        # automatically classify using solution
        classify(sol)

if __name__ == '__main__':
    main()