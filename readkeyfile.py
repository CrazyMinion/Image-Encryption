from PIL import Image
import numpy as np
def readkey(name,dim):
    path="keypic"
    im = Image.open((path+"/"+name))
    pixels = np.array(im)
    comp = pixels[0:dim[0],0:dim[1],:]
    return comp