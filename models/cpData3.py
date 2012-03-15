import os, sys, glob, shutil

ext    = '.png'
output = 'data3/'

if not os.path.exists(output):
    [os.makedirs(output+str(i)) for i in range(0,10)]
    
def getNewFilename(c):
    dst = output+str(c)+'/'
    files = [f for f in glob.glob(dst+'*'+ext)]
    if len(files):
        i = [int(os.path.basename(f).replace(ext, '')) for f in files]
        i.sort()
        i = i[-1]+1
    else:
        i = 0
    return dst+str(i)+ext
    
for input in ['data', 'data2']:
    for i in range(0,10):
        for f in glob.glob(input+'/'+str(i)+'/*'+ext):
            ff = getNewFilename(i)
            shutil.copy(f, ff)