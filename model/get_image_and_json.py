import json
import numpy as np
from PIL import Image

def get_image_and_json(img_path):
    img = np.array(Image.open(img_path))
    label_path = img_path.replace('png', 'json').replace('images', 'labels')
    if 'test_' in label_path:
        label_path=label_path.replace('pre', 'localization').replace('.json', '_prediction.json').replace('post', 'localization')
    with open(label_path) as label_file:
        label_data = json.load(label_file)
    return img, label_data
