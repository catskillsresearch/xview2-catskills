import numpy as np
from matplotlib.path import Path
from qhull_2d import *
from min_bounding_rect import *

def bounding_parallelipiped_of_bounding_polygon(polygon_geom):
    polygon_pts = np.array(list(polygon_geom.exterior.coords))    
    poly_path=Path(polygon_pts)
    hull_points = qhull2D(polygon_pts)[::-1]
    (rot_angle, area, width, height, center_point, corner_points) = minBoundingRect(hull_points)
    return width, height, corner_points
