import chainer.functions as F
from chainer import cuda
import numpy as np
from imantics import Mask
from predict_polygons import predict_polygons

def polygon_loss(score_cuda, n_gt_polygons):
    score1 = F.softmax(score_cuda)
    score1_cpu = cuda.to_cpu(score1.data)[0]
    building_mask_pred = (np.argmax(score1_cpu, axis=0) == 1)
    polygons_pred = Mask(building_mask_pred).polygons()
    n_polygons_pred = len(predict_polygons(polygons_pred))
    if n_gt_polygons == 0 and n_polygons_pred > 0:
        poly_loss = 1
    else: 
        poly_loss = abs(n_polygons_pred-n_gt_polygons)/n_gt_polygons
    return poly_loss, n_gt_polygons, n_polygons_pred
