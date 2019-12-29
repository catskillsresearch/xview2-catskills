#!/home/catskills/anaconda3/envs/xview2/bin/python

import glob, os, sys
from pred_vars import *
sys.path.append(f"{CODEDIR}/spacenet/inference")
import inference
from tqdm import tqdm
inference.localization_init()
files = glob.glob(f'{TESTDIR}/test_pre_*.png')
for pre_png in tqdm(files):
    image_id = pre_png.split('/')[-1].split('.')[0].split('_')[-1]
    out_local_json = f'{INFER_DIR}/test_localization_{image_id}_prediction.json'
    if os.path.isfile(out_local_json):
        continue
    inference.localize(pre_png, out_local_json)
