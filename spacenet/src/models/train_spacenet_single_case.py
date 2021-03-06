#!/usr/bin/env python
# coding: utf-8

# Overtrain Spacenet on each image one by one

import sys, glob, random
import numpy as np
from PIL import Image
import chainer
import chainer.functions as F
from chainer import cuda, serializers, Variable
from segmentation import SegmentationModel as Model
from rgb2gray import rgb2gray
from float_to_cpu import float_to_cpu
from polygon_loss_from_cuda_gt_mask import polygon_loss_from_cuda_gt_mask

DESKTOP='/home/catskills/Desktop'
DATA_DIR=f'{DESKTOP}/dataxv2'
CODE_DIR=f'{DESKTOP}/xview2-catskills'
MODEL_DIR=f'{DATA_DIR}/localization_overtrain'
TRAIN_DIR=f'{DATA_DIR}/train'

#weights=f'{DATA_DIR}/release/v_catskills_0.2.2/localization.hdf5'
weights=f'{MODEL_DIR}/model_ot3_12500.hdf5'

mean=f'{CODE_DIR}/weights/mean.npy'
mean = np.load(mean)
model = Model(weights, mean)

optimizer = chainer.optimizers.Adam()
optimizer.setup(model._SegmentationModel__model);

images=glob.glob(f'{TRAIN_DIR}/images/*')
random.shuffle(images)
train_iteration = 0

n_images = len(images)

for image_count, input in enumerate(images):
    image_name = input.split('/')[-1].split('.')[0].replace('_pre_disaster','')
    image = np.array(Image.open(input))
    image_in, crop = model._SegmentationModel__preprocess(image)

    trainfn = input.replace('/images/', '/gt_pred/')
    train = rgb2gray(np.array(Image.open(trainfn)))>0.5
    train_int = train.astype(int)
    gt=np.array([train_int])
    gt_in = Variable(cuda.cupy.asarray(gt, dtype=cuda.cupy.int))

    accuracy = 0
    image_iteration = 0
    float_loss = 100
    poly_loss = 100
    while image_iteration <= 100 and (poly_loss > 0.05 or float_loss > 2.0):
        with chainer.using_config('train', True):
            score_cuda= model._SegmentationModel__model.forward(image_in)
            loss = F.softmax_cross_entropy(score_cuda, gt_in)
            poly_loss = polygon_loss_from_cuda_gt_mask(score_cuda, gt_in)
            loss += 0.6*poly_loss
            accuracy=float_to_cpu(F.accuracy(score_cuda, gt_in))
            model._SegmentationModel__model.cleargrads()
            loss.backward()
            optimizer.update()
            image_iteration += 1
            train_iteration += 1
            float_loss = 100*float_to_cpu(loss)
            print(f'[{train_iteration} {image_iteration}; {image_count+1}/{n_images}] {image_name}: poly_loss {100*poly_loss:.3f}% loss {float_loss:.3f}% accuracy {100*accuracy:.2f}%')
            if train_iteration % 500 == 0:
                new_weights=f'{MODEL_DIR}/model_ot4_{train_iteration:05d}.hdf5'
                serializers.save_npz(new_weights, model._SegmentationModel__model)

