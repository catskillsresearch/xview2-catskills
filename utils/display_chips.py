
from PIL import Image, ImageDraw
from IPython.display import display
from shapely import wkt

damage_dict = {
        "no-damage": (0, 255, 0, 100),
        "minor-damage": (0, 0, 255, 125),
        "major-damage": (255, 69, 0, 125),
        "destroyed": (255, 0, 0, 125),
        "un-classified": (255, 255, 255, 125)
    }

damage_dict1 = {
        "no-damage": (0, 255, 0, 100),
        "minor-damage": (0, 255, 0, 100),
        "major-damage": (0, 255, 0, 100),
        "destroyed": (0, 255, 0, 100),
        "un-classified": (0, 255, 0, 100)
    }

damage_dict2 = {
        "no-damage": (255, 0, 0, 125),
        "minor-damage": (255, 0, 0, 125),
        "major-damage": (255, 0, 0, 125),
        "destroyed": (255, 0, 0, 125),
        "un-classified": (255, 0, 0, 125)
    }

def display_chips(path_to_image_value, coords):

    wkt_polygons = []

    for coord in coords:
        if 'subtype' in coord['properties']:
            damage = coord['properties']['subtype']
        else:
            damage = 'no-damage'
        wkt_polygons.append((damage, coord['wkt']))

    polygons = []

    for damage, swkt in wkt_polygons:
        polygons.append((damage, wkt.loads(swkt)))

    # Loading image
    img = Image.open(path_to_image_value)
    draw = ImageDraw.Draw(img, 'RGBA')


    for damage, polygon in polygons:
        x,y = polygon.exterior.coords.xy
        coords = list(zip(x,y))
        draw.polygon(coords, damage_dict[damage])

    del draw

    display(img)

def json_to_polygons(coords):

    wkt_polygons = []

    for coord in coords:
        if 'subtype' in coord['properties']:
            damage = coord['properties']['subtype']
        else:
            damage = 'no-damage'
        wkt_polygons.append((damage, coord['wkt']))

    polygons = []

    for damage, swkt in wkt_polygons:
        polygons.append((damage, wkt.loads(swkt)))

    return polygons

def draw_polygons(draw, polygons, damage_dict):

    for damage, polygon in polygons:
        x,y = polygon.exterior.coords.xy
        coords = list(zip(x,y))
        draw.polygon(coords, damage_dict[damage])

def display_chips2(path_to_image_value, gt, pred):

    polygons_gt = json_to_polygons(gt)
    polygons_pred = json_to_polygons(pred)
    
    # Loading image
    img = Image.open(path_to_image_value)
    draw = ImageDraw.Draw(img, 'RGBA')

    draw_polygons(draw, polygons_pred, damage_dict1)
    draw_polygons(draw, polygons_gt, damage_dict2)
    
    del draw

    display(img)
    
