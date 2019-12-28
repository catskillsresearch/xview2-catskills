import numpy as np
from skimage.transform import resize

def small_chip(img, H, W, scrds, crds):
    chip=np.zeros((H+1,W+1,3)).astype(img.dtype)
    for i in range(scrds.shape[0]):
        (xs,ys)=scrds[i]
        pixel=img[xs,ys]
        (xt,yt)=crds[i]
        chip[xt,yt]=pixel
    chip_small=resize(chip,(256,127),anti_aliasing=True)
    return chip_small
