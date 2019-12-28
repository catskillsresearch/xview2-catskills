#!/home/catskills/anaconda3/envs/xview2/bin/python

from IPython.utils.path import ensure_dir_exists
from pred_vars import *
ensure_dir_exists(SUBMIT_DIR)
ensure_dir_exists(INFER_DIR)

print('inference:', INFER_DIR)
print('submission:', SUBMIT_DIR)

