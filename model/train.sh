export DATADIR=/home/${USER}/Desktop/dataxv2/
export OLD_RELEASE=${DATADIR}release/v_catskills_0.0.1/
export BASE_MODEL=${OLD_RELEASE}classification.hdf5
export LOG_DIR=${DATADIR}logs/

python damage_classification.py \
       --train_data ${DATADIR}classifier_2x2 \
       --train_csv ${DATADIR}classifier_csv/train.csv \
       --test_data ${DATADIR}classifier_2x2 \
       --test_csv ${DATADIR}classifier_csv/test.csv \
       --model_out ${DATADIR}train_loc_model \
       --model_in ${BASE_MODEL}
