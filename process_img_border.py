import numpy as np

def process_img_border(img_array, polygon_pts, border=6):
    """Process Raw Data into

            Args:
                img_array (numpy array): numpy representation of image.
                polygon_pts (array): corners of the building polygon.

            Returns:
                numpy array: .

    """

    height, width, _ = img_array.shape

    xcoords = polygon_pts[:, 0]
    ycoords = polygon_pts[:, 1]
    xmin, xmax = np.min(xcoords), np.max(xcoords)
    ymin, ymax = np.min(ycoords), np.max(ycoords)

    xdiff = xmax - xmin
    ydiff = ymax - ymin

    #Extend image by scale percentage
    xmin = max(int(xmin - border), 0)
    xmax = min(int(xmax + border), width)
    ymin = max(int(ymin - border), 0)
    ymax = min(int(ymax + border), height)

    (X,Y,Z)=img_array.shape
    
    return img_array[ymin:ymax, xmin:xmax, :]
