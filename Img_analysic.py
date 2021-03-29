import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import os
os.environ['PROJ_LIB'] = 'C:\\Users\\gheom\\.spyder-py3\\'

im_orig = Image.open('marinesnow3.jpg')
#print(np.array(im_orig).shape)

im_bw = im_orig.convert('L')
im = np.array(im_bw)
plt.imshow(im, cmap ='gray')

print(im.shape)

U, s, V = np.linalg.svd(im)

#plt.imshow(im_recon, cmap='gray')

reconstimg = np.matrix(U[:,:40]) *np.diag(s[:40]) * np.matrix(V[:40,:])
plt.imshow(reconstimg, cmap = 'gray')
