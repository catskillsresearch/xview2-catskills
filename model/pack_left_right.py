import numpy as np

def pack_left_right(chip_pre_small, chip_post_small):
    # Chip 256x256 pre on left, post on right
    chip=np.zeros((256,256,3)).astype(chip_pre_small.dtype)
    chip[:,0:127,:]=chip_pre_small*255
    chip[:,129:,:]=chip_post_small*255
    return chip
