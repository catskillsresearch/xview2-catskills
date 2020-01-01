#!/home/catskills/anaconda3/envs/xview2/bin/python

from IPython.utils.path import ensure_dir_exists
from pred_vars import *

for x in [VDIR,
          TESTDIR,
          INFER_DIR,
          POLYDIR,
          PREDICTION,
          COMBINED_JSON]:
    ensure_dir_exists(x)
    print(x)
