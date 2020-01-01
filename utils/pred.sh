export VERSION=0.2.2
python pred_preamble.py
#python pred_localization.py
#python pred_extract_polygons.py
#python pred_damage.py
#python pred_combine_jsons.py
#python pred_json_to_png.py
cd /home/catskills/Desktop/dataxv2/v_catskills_${VERSION}/prediction
export SUBMISSION=../submit_v_catskills_${VERSION}_submit_001.tar.gz
tar cvfz ${SUBMISSION} *.png
ls -l ${SUBMISSION}
