#!/home/catskills/anaconda3/envs/xview2/bin/python

import sys
from pred_vars import *
sys.path.append(f"{CODEDIR}/model")
from damage_training_chip_formatting import damage_training_chip_formatting

damage_training_chip_formatting(TESTDIR, POLYDIR, OUTPUT_CSV)
