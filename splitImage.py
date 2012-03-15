import Image, ImageDraw, ImageFont, ImageStat
import random, os, shutil

input = 'cv/sudoku.png'
out = 'input/'
tmp = out+'all/'
targetsize = 20
m = 0
threshold = 250 # brighter fields are empty

if not os.path.exists(input):
    print input+' is missing! Capture image using cv.exe first.'
    exit()

if os.path.exists(out):
    shutil.rmtree(out)
os.makedirs(tmp)

def within(img, x, y):
    w, h = img.size
    return x >= 0 and x < w and y >= 0 and y < h

BORDER_COLOR = 200
def flood_fill(img, x, y, value):
    "Flood fill on a region of non-BORDER_COLOR pixels."
    p = img.load()
    if not within(img, x, y) or p[x, y] >= 250:
        return
    edge = [(x, y)]
    p[x, y] = value
    while edge:
        newedge = []
        for (x, y) in edge:
            for (s, t) in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                if within(img, s, t) and p[s, t] < BORDER_COLOR: #abs(org - p[s, t]) < 50: #not in (BORDER_COLOR, value):
                        # print s, t, p[s, t], value
                        p[s, t] = value
                        newedge.append((s, t))
        edge = newedge

FILL = 255
def process(img):
    "flood fill white in every corner to remove unwanted edges"
    # better: http://packages.python.org/mahotas
    size = img.size[0]
    
    # for o in range(2): # fill from corners going inwards with an offset o
        # s = size-o-1
        # flood_fill(img, o, o, FILL)
        # flood_fill(img, s, o, FILL)
        # flood_fill(img, o, s, FILL)
        # flood_fill(img, s, s, FILL)

    for o in range(2): # go around all edges
        for i in range(size):
            flood_fill(img, o, i, FILL)
            flood_fill(img, i, size-o, FILL)
            flood_fill(img, size-o, i, FILL)
            flood_fill(img, i, o, FILL)

    img.thumbnail((targetsize, targetsize), Image.ANTIALIAS)
    return img

def brightness(img):
   im = img.convert('L')
   stat = ImageStat.Stat(im)
   return stat.mean[0]

def mean(nums):
    return float(sum(nums) / len(nums)) if len(nums) else 0.0

img = Image.open(input)
# img.thumbnail((9*size, 9*size), Image.ANTIALIAS)
# img.save(tmp+'resized.png', 'PNG')
size = img.size[0]/9
histogram = []
for i in range(9*9):
    row = i%9
    col = i/9
    x = int(row*size)
    y = int(col*size)
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
print 'Mean: ', mean(histogram)