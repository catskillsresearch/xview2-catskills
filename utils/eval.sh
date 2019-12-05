#!/bin/bash

set -x

export DISASTER=santa-rosa-wildfire
export IMAGEID=00000030

./inference.sh \
    -x /home/catskills/Desktop/crcxv2 \
    -i /home/catskills/Desktop/dataxv2/xBD/${DISASTER}/images/${DISASTER}_${IMAGEID}_pre_disaster.png \
    -p /home/catskills/Desktop/dataxv2/xBD/${DISASTER}/images/${DISASTER}_${IMAGEID}_post_disaster.png \
    -l /home/catskills/Desktop/crcxv2/spacenet/models/logs/model_iter_10700 \
    -c /home/catskills/Desktop/dataxv2/model2-saved-model-13-0.92.hdf5 \
    -o ~/Desktop/crcxv2/utils/larswe1.png -y
