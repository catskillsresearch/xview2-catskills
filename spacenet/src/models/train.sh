#!/usr/bin/bash -x

export DATA_DIR=/home/catskills/Desktop/dataxv2
export SPACE_DIR=${DATA_DIR}/spacenet_gt
export BASE_SNAPSHOT=${DATA_DIR}/localization_models/snapshot_iter_10700
export MODELS=${SPACE_DIR}/models
mkdir -p ${MODELS}

python train_model.py ${SPACE_DIR}/dataSet/ ${SPACE_DIR}/images/ ${SPACE_DIR}/labels/ -b 1 -B 1 --out ${MODELS} -e 1
