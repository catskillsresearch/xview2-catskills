#!/home/catskills/anaconda3/envs/xview2/bin/python

import shutil, glob
from subprocess import call
from IPython.utils.path import ensure_dir_exists

VERSION='v_catskills_0.0.0'
PROJECT='xview2-catskills'
USERDIR='/home/catskills/Desktop/'
CODEDIR=f'{USERDIR}{PROJECT}'
DATADIR=f'{USERDIR}dataxv2/'
TESTDIR=f'{DATADIR}test/images/'
SUBMIT_DIR=f'{DATADIR}catskills_0.0.0_submit_001'
MODEL_DIR='/home/catskills/Desktop/dataxv2/release/v_catskills_0.0.0/'
LOCALIZATION_MODEL=f'{MODEL_DIR}localization.hdf5'
DAMAGE_MODEL=f'{MODEL_DIR}classification.hdf5'

ensure_dir_exists(SUBMIT_DIR)


files = glob.glob(f'{TESTDIR}test_pre_*.png')

for pre_png in tqdim(files):
    post_png = pre_png.replace('_pre_','_post_')
    image_id = pre_png.split('.')[0].split('/')[-1].split('_')[-1]
    out_local_json = f'{SUBMIT_DIR}/test_localization_{image_id}_prediction.json'
    out_local_png = f'{SUBMIT_DIR}/test_localization_{image_id}_prediction.png'
    out_damage_png = f'{SUBMIT_DIR}/test_damage_{image_id}_prediction.png'
    C=f'./inference.sh -x {CODEDIR} -i {pre_png} -p {post_png} -l {LOCALIZATION_MODEL} -c {DAMAGE_MODEL} -o {out_damage_png} -y'
    call(C, shell=True)
    shtuil.copyfile(out_damage_png, out_local_png)
