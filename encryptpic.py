from PIL import Image
import numpy as np
from readkeyfile import readkey

name="minion"             #change the name of picture

format=".jpg"                                #change the format accordingly
from_path="pics_to_hide/"
to_path="pics_after_hide/"
key_path="keypic"
keyname="keyfilepic.png"
im = Image.open(from_path+name+format)
pixels = np.array(im)
dim = pixels.shape
comp = readkey(keyname, dim)
newpixels = (pixels ^ comp)
print(pixels.dtype)
newimg = Image.fromarray(newpixels)
encrypt_format=".png"   #lossless keep fixed
newimg.save(to_path+'cpl_' + name+encrypt_format)
newimg.show()