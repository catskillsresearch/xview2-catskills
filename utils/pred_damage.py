#!/home/catskills/anaconda3/envs/xview2/bin/python

import sys
from pred_vars import *
sys.path.append(f"{CODEDIR}/model")
from damage_inference import run_inference

run_inference(POLYDIR, OUTPUT_CSV, DAMAGE_MODEL, DAMAGE_JSON)
