import cv2
import numpy as np
from bounding_parallelipiped_of_bounding_polygon import bounding_parallelipiped_of_bounding_polygon
from transform_bounding_parallelipiped_to_bounding_square import transform_bounding_parallelipiped_to_bounding_square
from small_chip import small_chip
from pack_left_right import pack_left_right

def mask_out_image_and_rotate_to_minimum_area_chip_feature(output_dir, uid, polygon_geom, img_pre, img_post):
    width, height, corner_points = bounding_parallelipiped_of_bounding_polygon(polygon_geom)
    H, W, scrds, crds  = transform_bounding_parallelipiped_to_bounding_square(width, height, corner_points)
    chip_pre_small = small_chip(img_pre, H, W, scrds, crds)
    chip_post_small = small_chip(img_post, H, W, scrds, crds)
    chip = pack_left_right(chip_pre_small, chip_post_small)
    cv2.imwrite(output_dir + "/" + uid + ".png", chip)
