from PIL import Image
import numpy as np
from readkeyfile import readkey

name="minion"     #change  this

fromformat=".png"
from_path="pics_after_hide/"
to_path="pics_recovered/"
toformat=".jpeg"
keyname="keyfilepic.png"
im = Image.open(from_path+'cpl_'+name+fromformat)
pixels = np.array(im)
dim = pixels.shape
comp = readkey(keyname, dim)
newpixels = (pixels ^ comp)
newimg = Image.fromarray(newpixels)
encrypt_format=".png"   #lossless keep fixed
newimg.save(to_path+'recovered_' + name+toformat)
newimg.show()