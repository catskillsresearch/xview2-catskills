DISASTER='santa-rosa-wildfire'
IMAGEID='00000030'
XBD='/home/catskills/Desktop/dataxv2/xBD'
im_reference=XBD+'/'+DISASTER+'/images/'+DISASTER+'_'+IMAGEID+'_pre_disaster.png'
im_target=XBD+'/'+ DISASTER+'/images/'+DISASTER+'_'+IMAGEID+'_post_disaster.png'
from arosics import COREG
CR = COREG(im_reference, im_target)
CR.calculate_spatial_shifts()
