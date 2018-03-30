#key for encryption

from PIL import Image
import numpy as np
to_path="keypic/"
to_format=".png"
name='keyfilepic'
dim=[5000, 5000, 3]
comp=np.random.randint(256,size=(dim[0],dim[1],dim[2]))
comp=comp.astype(np.uint8)
newimg= Image.fromarray(comp)
newimg.save(to_path+name+to_format)
newimg.show()