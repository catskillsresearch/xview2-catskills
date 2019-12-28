#!/home/catskills/anaconda3/envs/xview2/bin/python

import sys, json, glob, tqdm
from shutil import copyfile
from subprocess import call
from pred_vars import *
from inference_image_output import create_inference_image

for pred_json_fn in tqdm.tqdm(glob.glob(f'{COMBINED_JSON}/*.json')):
    out_damage_png = pred_json_fn.replace('/combined_json/', '/prediction/').replace('.json', '.png')
    out_local_png = out_damage_png.replace('localization', 'damage')
    create_inference_image(pred_json_fn, out_damage_png)
    copyfile(out_damage_png, out_local_png)
