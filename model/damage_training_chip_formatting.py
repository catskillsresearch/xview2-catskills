#!/usr/bin/env python
# coding: utf-8

import os, glob
from p_tqdm import p_map
from mask_out_image_and_rotate_to_minimum_area_chip import mask_out_image_and_rotate_to_minimum_area_chip
import pandas as pd

def damage_training_chip_formatting(image_path, output_dir, output_csv):
    img_paths=glob.glob(f'{image_path}/*_post_*.png')
    try:
        os.makedirs(output_dir)
    except:
        pass

    L = p_map(lambda img_path: mask_out_image_and_rotate_to_minimum_area_chip(img_path, output_dir), img_paths)
    x_data = []
    for ell in L:
        x_data.extend(ell)
    data_array = {'uuid': x_data}
    df = pd.DataFrame(data = data_array)
    df.to_csv(output_csv)

if __name__=="__main__":
    image_path='/home/catskills/Desktop/dataxv2/xBD/*/images'
    output_dir='/home/catskills/Desktop/dataxv2/classifier_2x2'
    output_csv = '/tmp/output.csv'
    damage_training_chip_formatting(image_path, output_dir, output_csv)
