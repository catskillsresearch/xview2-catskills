import numpy as np
from skimage.transform import ProjectiveTransform

def transform_bounding_parallelipiped_to_bounding_square(width, height, corner_points):
    t = ProjectiveTransform()
    src = corner_points[0:-1]
    dst = np.asarray([[0, 0], [0, 1], [1, 1], [1, 0]])
    if not t.estimate(src, dst): raise Exception("estimate failed")
    H=np.ceil(height).astype(int)
    W=np.ceil(width).astype(int)
    x2, y2 = np.mgrid[:H, :W]
    crds=np.hstack((x2.reshape(-1, 1), y2.reshape(-1,1))).astype(int)
    crds1 = crds/np.array([H,W])
    scrds=np.minimum(np.round(t.inverse(crds1)[:,::-1]).astype(int), 1023)
    return H, W, scrds, crds
