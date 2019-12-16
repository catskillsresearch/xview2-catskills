#!/bin/bash

set -x

export DISASTER=santa-rosa-wildfire
export IMAGEID=00000030
export CODE_DIR=/home/catskills/Desktop/xview2-catskills
export DATA_DIR=/home/catskills/Desktop/dataxv2
export MODEL_DIR=${DATA_DIR}/release/v_catskills_0.0.0
export LOCALIZATION_MODEL=${MODEL_DIR}/localization.hdf5
export DAMAGE_MODEL=${MODEL_DIR}/classification.hdf5
export PRE_IMAGE_SRC=/home/catskills/Desktop/dataxv2/xBD/${DISASTER}/images/${DISASTER}_${IMAGEID}_pre_disaster.png
export POST_IMAGE_SRC=/home/catskills/Desktop/dataxv2/xBD/${DISASTER}/images/${DISASTER}_${IMAGEID}_post_disaster.png
export PRE_JSON_SRC=/home/catskills/Desktop/dataxv2/xBD/${DISASTER}/labels/${DISASTER}_${IMAGEID}_pre_disaster.json
export POST_JSON_SRC=/home/catskills/Desktop/dataxv2/xBD/${DISASTER}/labels/${DISASTER}_${IMAGEID}_post_disaster.json
export TESTCASE_DIR=${DATA_DIR}/scoretest
export TESTCASE_PRED=${TESTCASE_DIR}/predictions
export TESTCASE_TGT=${TESTCASE_DIR}/targets
export TESTCASE_SCORE=${TESTCASE_DIR}/score.json
export PRED_DAMAGE_PNG=${TESTCASE_PRED}/test_damage_00000_prediction.png
export PRED_LOCAL_PNG=${TESTCASE_PRED}/test_localization_00000_prediction.png
export TGT_DAMAGE_PNG=${TESTCASE_TGT}/test_damage_00000_target.png
export TGT_LOCAL_PNG=${TESTCASE_TGT}/test_localization_00000_target.png

mkdir -p ${TESTCASE_PRED}
mkdir -p ${TESTCASE_TGT}

./infer.sh -x ${CODE_DIR} -i ${PRE_IMAGE_SRC} -p ${POST_IMAGE_SRC} -l ${LOCALIZATION_MODEL} -c ${DAMAGE_MODEL} -o ${PRED_DAMAGE_PNG} -y

cp ${PRED_DAMAGE_PNG} ${PRED_LOCAL_PNG}

python ${CODE_DIR}/utils/inference_image_output.py --input ${POST_JSON_SRC} --output ${TGT_DAMAGE_PNG}

cp ${TGT_DAMAGE_PNG} ${TGT_LOCAL_PNG} 

python xview2_metrics.py --pred_dir ${TESTCASE_PRED} --targ_dir ${TESTCASE_TGT} --out_fp ${TESTCASE_SCORE}

ls ${PRE_JSON_SRC}
ls ${POST_JSON_SRC}
