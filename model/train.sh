export DATADIR=/home/${USER}/Desktop/dataxv2/
export OLD_RELEASE=${DATADIR}release/v_catskills_0.0.0/
export BASE_MODEL=${OLD_RELEASE}classification.hdf5
export LOG_DIR=${DATADIR}logs/

python damage_classification.py \
       --train_data ${DATADIR}classifier \
       --train_csv ${DATADIR}classifier/csv/train.csv \
       --test_data ${DATADIR}classifier \
       --test_csv ${DATADIR}classifier/csv/test.csv \
       --model_out ${DATADIR}train_loc_model \
       --model_in ${BASE_MODEL}
