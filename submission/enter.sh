#!/bin/bash -x

sudo docker run \
     -v /home/catskills/Desktop/dataxv2/xBD/:/submission/ \
     -v /home/catskills/Desktop/dataxv2/output/:/output/ \
     -it --entrypoint=/bin/bash catskills-xview2-0.0.0

