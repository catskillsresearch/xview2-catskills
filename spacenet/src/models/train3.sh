#!/usr/bin/bash -x

export VERSION=v_catskills_0.2.1
export MODEL_DIR=/home/catskills/Desktop/dataxv2/release/${VERSION}
export LOCALIZATION_MODEL=${MODEL_DIR}/localization.hdf5
export DATA_DIR=/home/catskills/Desktop/dataxv2
export MEAN=/home/catskills/Desktop/xview2-catskills/weights/mean.npy
export SPACE_DIR=${DATA_DIR}/spacenet_gt_whole
export BASE_MODEL=${SPACE_DIR}/snapshot_iter_109568

mkdir -p ${SPACE_DIR}

python train_model3.py ${SPACE_DIR}/dataSet/ ${SPACE_DIR}/images/ ${SPACE_DIR}/labels/ --out ${SPACE_DIR} -e 300 --resume ${BASE_MODEL}
