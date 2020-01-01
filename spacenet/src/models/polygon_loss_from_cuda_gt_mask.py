import chainer.functions as F
from chainer import cuda
import numpy as np
from imantics import Mask
from predict_polygons import predict_polygons
import cupy

def polygon_loss_from_cuda_gt_mask(score_cuda, gt_mask_cuda):
    try:
        gt_mask=cuda.to_cpu(gt_mask_cuda)[0]
    except:
        gt_mask=cuda.to_cpu(gt_mask_cuda.data)[0]

    gt_mask=gt_mask.astype(bool)

    score1 = F.softmax(score_cuda)
    score1_cpu = cuda.to_cpu(score1.data)[0]

    building_mask_pred = (np.argmax(score1_cpu, axis=0) == 1)
    pred_polygons = Mask(building_mask_pred).polygons()
    n_pred_polygons = len(predict_polygons(pred_polygons))

    polygons_gt = Mask(gt_mask).polygons()
    n_gt_polygons = len(predict_polygons(polygons_gt))

    if n_gt_polygons == 0:
        if n_pred_polygons == 0:
            poly_loss = 0.0
        else:
            poly_loss = 1.0
    else: 
        poly_loss = abs(n_pred_polygons-n_gt_polygons)/n_gt_polygons

    return poly_loss
