import Image, ImageDraw, ImageFont, ImageStat
import random, os, shutil

input = 'cv/sudoku.png'
out = 'input/'
tmp = out+'tmp/'
size = 20
m = 0
threshold = 240 # brighter fields are empty

if not os.path.exists(input):
    print input+' is missing! Capture image using cv.exe first.'
    exit()

if os.path.exists(out):
    shutil.rmtree(out)
os.makedirs(tmp)

def within(img, x, y):
    w, h = img.size
    return x >= 0 and x < w and y >= 0 and y < h

BORDER_COLOR = 240
def flood_fill(img, x, y, value):
    "Flood fill on a region of non-BORDER_COLOR pixels."
    p = img.load()
    if not within(img, x, y) or p[x, y] >= BORDER_COLOR:
        return
    edge = [(x, y)]
    p[x, y] = value
    while edge:
        newedge = []
        for (x, y) in edge:
            for (s, t) in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                if within(img, s, t) and p[s, t] < BORDER_COLOR: #not in (BORDER_COLOR, value):
                    # print s, t, p[s, t], value
                    p[s, t] = value
                    newedge.append((s, t))
        edge = newedge

def process(img):
    "flood fill white in every corner to remove unwanted edges"
    # better: http://packages.python.org/mahotas
    o = 0
    s = size-o-1
    flood_fill(img, o, o, 255)
    flood_fill(img, s, o, 255)
    flood_fill(img, o, s, 255)
    flood_fill(img, s, s, 255)
    return img

def brightness(img):
   im = img.convert('L')
   stat = ImageStat.Stat(im)
   return stat.mean[0]

img = Image.open(input)
img.thumbnail((9*size, 9*size), Image.ANTIALIAS)
img.save(tmp+'resized.png', 'PNG')
histogram = []
for i in range(9*9):
    row = i%9
    col = i/9
    x = row*size
    y = col*size
    cropped = img.crop((x+m, y+m, x+size-m, y+size-m))
    cropped = process(cropped)
    file = str(i+1)+'.png'
    cropped.save(tmp+file, 'PNG')
    
    b = brightness(cropped)
    histogram.append(b)
    if b > threshold:
        print file, ' is empty'
    else:
        cropped.save(out+file, 'PNG')
histogram.sort()
print 'Mean brightness for all fields: ', histogram
print 'Median: ', histogram[len(histogram)/2]