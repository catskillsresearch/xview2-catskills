#!/home/catskills/anaconda3/envs/xview2/bin/python

import sys, json, glob
from pred_vars import *

def combine_output(LOCALIZE_JSON, DAMAGE_JSON):
    """
    :param LOCALIZE_JSON: the file path to the localization inference output json  
    :param DAMAGE_JSON_classification: the file path to the classification inference output json
    :param PRED_JSON: the file path to store the combined json file
    """

    with open(DAMAGE_JSON) as damages:
        label_json = json.load(damages)

    polygon_jsons = glob.glob(f"{LOCALIZE_JSON}/*.json")
    for pred_polygons in polygon_jsons:

        # Skeleton of the json with null values 
        output_json = {
            "features": {
                "lng_lat": [],
                "xy": []
            }, 
            "metadata": {
                "sensor": "",
                "provider_asset_type": "",
                "gsd": 0,
                "capture_date": "", 
                "off_nadir_angle": 0, 
                "pan_resolution": 0, 
                "sun_azimuth": 0, 
                "sun_elevation": 0, 
                "target_azimuth": 0, 
                "disaster": "", 
                "disaster_type": "", 
                "catalog_id": "", 
                "original_width": 0, 
                "original_height": 0, 
                "width": 0, 
                "height": 0, 
                "id": "", 
                "img_name": ""
            }
        }
        # Open the localization json 
        with open(pred_polygons) as polys:
            poly_json = json.load(polys)

        PRED_JSON = pred_polygons.replace('/labels/', '/combined_json/')
        # Match UUIDs from the two jsons and combine in output_json skeleton 
        for p in poly_json['features']['xy']:
            p['properties']['subtype'] = label_json[p['properties']['uid']]
            output_json['features']['xy'].append(p)
    
        # Finally save out the combined json file 
        with open(PRED_JSON, 'w') as out: 
            json.dump(output_json, out, indent=4)

if __name__=='__main__':
    combine_output(INFER_DIR, DAMAGE_JSON)
