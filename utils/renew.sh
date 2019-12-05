
python split_into_disasters.py --input ../../xview2_stage/train/ --output ../../xview2_stage/xBD
python mask_polygons.py --input ../../dataxv2/xBD --single-file --border 2
mkdir ../../dataxv2/xBD/spacenet_gt/masks
data_finalize.sh -i /home/catskills/Desktop/dataxv2/xBD/ -x /home/catskills/Desktop/crcxv2/ -s .75
