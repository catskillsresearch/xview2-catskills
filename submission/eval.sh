#!/bin/bash

set -x

export DISASTER=santa-rosa-wildfire
export IMAGEID=00000030
export TAG=catskills-xview2-0.0.0
export PREIMAGE=/submission/${DISASTER}/images/${DISASTER}_${IMAGEID}_pre_disaster.png
export POSTIMAGE=/submission/${DISASTER}/images/${DISASTER}_${IMAGEID}_post_disaster.png

mkdir -p /home/catskills/Desktop/dataxv2/output/test

sudo docker run \
     -v /home/catskills/Desktop/dataxv2/xBD/:/submission/ \
     -v /home/catskills/Desktop/dataxv2/output/:/output/ \
     ${TAG} ${PREIMAGE} ${POSTIMAGE} \
     /output/test/loc.png /output/test/dmg.png
