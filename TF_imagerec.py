##########################################
# image recognition - by sent dex
##########################################

# result [RED, GREEN, BLUE, Alapha(Transparent)]
# [0 0 0 255] means -> black
# [255 255 255 255] means -> white
# 8x8 pixel image 
# black white white white white white white white
# while white white white white white white white
# while white white white white white white white
# while white white white white white white white
# while white white white white white white white
# while white white white white white white white
# while white white white white white white white
# while white white white white white white white
# [[[  0   0   0 255], [255 255 255 255], [255 255 255 255], [255 255 255 255], [255 255 255 255], [255 255 255 255], [255 255 255 255], [255 255 255 255]]
#  [[255 255 255 255], [255 255 255 255], [255 255 255 255], [255 255 255 255], [255 255 255 255], [255 255 255 255], [255 255 255 255], [255 255 255 255]]
#  [[255 255 255 255], [255 255 255 255], [255 255 255 255], [255 255 255 255], [255 255 255 255], [255 255 255 255], [255 255 255 255], [255 255 255 255]]
#  [[255 255 255 255], [255 255 255 255], [255 255 255 255], [255 255 255 255], [255 255 255 255], [255 255 255 255], [255 255 255 255], [255 255 255 255]]
#  [[255 255 255 255], [255 255 255 255], [255 255 255 255], [255 255 255 255], [255 255 255 255], [255 255 255 255], [255 255 255 255], [255 255 255 255]]
#  [[255 255 255 255], [255 255 255 255], [255 255 255 255], [255 255 255 255], [255 255 255 255], [255 255 255 255], [255 255 255 255], [255 255 255 255]], 
#  [[255 255 255 255], [255 255 255 255], [255 255 255 255], [255 255 255 255], [255 255 255 255], [255 255 255 255], [255 255 255 255], [255 255 255 255]]
#  [[255 255 255 255], [255 255 255 255], [255 255 255 255], [255 255 255 255], [255 255 255 255], [255 255 255 255], [255 255 255 255], [255 255 255 255]]]

# download zip from sentdex.com/imagetutorial.zip

# if you're on 32bit OS:
# import Image

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

#i = Image.open('C:/work/python/images/dotline.png')
i = Image.open('C:/work/python/images/numbers/0.1.png')
iar = np.asarray(i)
#print(iar)
plt.imshow(iar)
plt.show()
