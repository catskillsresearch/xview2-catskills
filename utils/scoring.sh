#!/bin/bash

set -x

export DISASTER=santa-rosa-wildfire
export IMAGEID=00000030
export MODEL_DIR=/home/catskills/Desktop/dataxv2/release/v_catskills_0.0.0/
export LOCALIZATION_MODEL=${MODEL_DIR}/localization.hdf5
export DAMAGE_MODEL=${MODEL_DIR}/classification.hdf5

./inference.sh \
    -x /home/catskills/Desktop/crcxv2 \
    -i /home/catskills/Desktop/dataxv2/xBD/${DISASTER}/images/${DISASTER}_${IMAGEID}_pre_disaster.png \
    -p /home/catskills/Desktop/dataxv2/xBD/${DISASTER}/images/${DISASTER}_${IMAGEID}_post_disaster.png \
    -l ${LOCALIZATION_MODEL} \
    -c ${DAMAGE_MODEL} \
    -o ~/Desktop/crcxv2/utils/larswe1.png -y
