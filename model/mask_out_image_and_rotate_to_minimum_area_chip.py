import os
import shapely.wkt
from get_image_and_json import get_image_and_json
from mask_out_image_and_rotate_to_minimum_area_chip_feature import mask_out_image_and_rotate_to_minimum_area_chip_feature

def mask_out_image_and_rotate_to_minimum_area_chip(img_path_post, output_dir):
    img_pre, label_pre = get_image_and_json(img_path_post.replace('_post_', '_pre_'))
    img_post, label_post = get_image_and_json(img_path_post)
    x_data = []
    for feat_pre, feat_post in zip(label_pre['features']['xy'], label_post['features']['xy']):
        uid = feat_post['properties']['uid']
        if feat_pre['properties']['uid'] != uid:
            raise ValueError('shouldnt happen')
        polygon_geom = shapely.wkt.loads(feat_pre['wkt'])
#        mask_out_image_and_rotate_to_minimum_area_chip_feature(output_dir, uid, polygon_geom, img_pre, img_post)
        poly_uuid = f"{uid}.png"
        x_data.append(poly_uuid)
    return x_data

