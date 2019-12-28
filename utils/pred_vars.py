USERDIR='/home/catskills/Desktop'

DATADIR=f'{USERDIR}/dataxv2'

PROJECT='xview2-catskills'
CODEDIR=f'{USERDIR}/{PROJECT}'

VERSION='v_catskills_0.2.0'
MODEL_DIR=f'/home/catskills/Desktop/dataxv2/release/{VERSION}'
LOCALIZATION_MODEL=f'{MODEL_DIR}/localization.hdf5'
DAMAGE_MODEL=f'{MODEL_DIR}/classification.hdf5'
MEAN_MODEL=f'{CODEDIR}/weights/mean.npy'

VDIR=f'{DATADIR}/{VERSION}'
TESTDIR=f'{VDIR}/images'
INFER_DIR=f'{VDIR}/labels'
POLYDIR=f'{VDIR}/damage_input'
SUBMIT_DIR=f'{VDIR}/submit'
OUTPUT_CSV=f'{VDIR}/output.csv'
DAMAGE_JSON=f'{VDIR}/damage.json'
COMBINED_JSON=f'{VDIR}/combined_json'

