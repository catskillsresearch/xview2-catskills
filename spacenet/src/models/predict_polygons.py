from simplification.cutil import simplify_coords_vwp

def predict_polygons(polygons):
    new_predictions = []
    for poly in polygons:
        if len(poly) >= 3:
            f = poly.reshape(-1, 2)
            simplified_vw = simplify_coords_vwp(f, .3)
            if len(simplified_vw) > 2:
                    mpoly = []
                    # Rebuilding the polygon in the way that PIL expects the values [(x1,y1),(x2,y2)]
                    for i in simplified_vw:
                        mpoly.append((i[0], i[1]))
                    # Adding the first point to the last to close the polygon
                    mpoly.append((simplified_vw[0][0], simplified_vw[0][1]))
                    new_predictions.append(mpoly)
    return new_predictions
