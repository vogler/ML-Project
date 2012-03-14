import numpy as np
from scipy import ndimage
import mahotas
import pylab

img = mahotas.imread('1.png')
T_otsu = mahotas.thresholding.otsu(img)
seeds,_ = ndimage.label(img > T_otsu)
labeled = mahotas.cwatershed(img.max() - img, seeds)

pylab.imshow(labeled)