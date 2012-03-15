import os, sys, glob, shutil
import Image, ImageDraw, ImageFont, ImageStat
import numpy, pylab
import matplotlib.pyplot as plt

ext    = '.png'
input  = 'input/*'+ext
output = 'data2/'
cv_img = 'cv/sudoku.png'
if not os.path.exists(output):
    [os.makedirs(output+str(i)) for i in range(0,10)]

print "This program will (in a loop) start cv.exe to capture an image (hit 'c'), split it and then ask you to classify the numbers."
print "Enter 0 for empty fields"

def show(img):
    # imgplot = plt.imshow(img)
    # plt.show()
    img.show() # PIL

def number_input():
    while True:
        try:
            c = int(raw_input('Enter number: '))
            if c < 0 or c > 9: raise ValueError
            return c
        except ValueError:
            print 'Number has to be 0-9 (0 for empty fields)!'

def getNewFilename(c):
    dst = output+str(c)+'/'
    files = [f for f in glob.glob(dst+'*'+ext)]
    files.sort()
    if len(files):
        lastFile = files[-1]
        basename = os.path.basename(lastFile).replace(ext, '')
        i = int(basename)+1
    else:
        i = 0
    return dst+str(i)+ext

def classify():
    print 'Please classify (0-9), 0 for empty field.'
    plt.show()
    for f in glob.glob(input):
        img = Image.open(f)
        show(img)
        c = number_input()
        shutil.move(f, getNewFilename(c))

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
    os.system('python split-image.py')
    # ask user to classify images until input is empty
    classify()