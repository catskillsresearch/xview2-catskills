from PIL import Image
import numpy as np
from segmentation3 import SegmentationModel as Model
import chainer, cv2, sys
import chainer.functions as F
from chainer import cuda, serializers, Variable
from polygon_loss import polygon_loss
from float_to_cpu import float_to_cpu
from polygon_loss import polygon_loss
from rgb2gray import rgb2gray

sys.path.append('/home/catskills/Desktop/xview2-catskills/utils')
sys.path.append('../src/models')

input='/home/catskills/Desktop/dataxv2/xBD/santa-rosa-wildfire/images/santa-rosa-wildfire_00000030_pre_disaster.png'
trainfn='/home/catskills/Desktop/dataxv2/xBD/santa-rosa-wildfire/masks/santa-rosa-wildfire_00000030_pre_disaster.png'
weights='/home/catskills/Desktop/dataxv2/release/v_catskills_0.2.1/localization.hdf5'
mean='/home/catskills/Desktop/xview2-catskills/weights/mean.npy'
mean = np.load(mean)
model = Model(weights, mean)
image = np.array(Image.open(input))
train=np.array(Image.open(trainfn))
train = rgb2gray(np.array(Image.open(trainfn)))>0.5
score = model.apply_segmentation(image)
building_mask_pred = (np.argmax(score, axis=0) == 1)
bm_only = (building_mask_pred & ~train).astype(int)*9
train_only=(train & ~building_mask_pred).astype(int)*3
bm_and_tr=(building_mask_pred & train).astype(int)*6
all = bm_only + train_only + bm_and_tr
optimizer = chainer.optimizers.Adam()
optimizer.setup(model._SegmentationModel__model);
train_int = train.astype(int)
gt=np.array([train_int])
gt_in = Variable(cuda.cupy.asarray(gt, dtype=cuda.cupy.int))
image_in, crop = model._SegmentationModel__preprocess(image)
gt_polygons = Mask(train).polygons()
n_gt_polygons = len(predict_polygons(gt_polygons))
for i in range(10):
    with chainer.using_config('train', True):
        score_cuda = model._SegmentationModel__model.forward(image_in)
        loss = F.softmax_cross_entropy(score_cuda, gt_in)    
        poly_loss, n_gt, n_pred = polygon_loss(score_cuda, n_gt_polygons)
        softmax_loss = float_to_cpu(loss)
        loss += 0.4*poly_loss
        accuracy=float_to_cpu(F.accuracy(score_cuda, gt_in))
        print(f'[{i}] n_gt {n_gt} n_pred {n_pred} poly_loss {100*poly_loss:.1f}% softmax_loss {100*softmax_loss:.1f}% loss {100*float_to_cpu(loss):.3f}% accuracy {100*accuracy:.6f}%')
        model._SegmentationModel__model.cleargrads()
        loss.backward()
        optimizer.update()
