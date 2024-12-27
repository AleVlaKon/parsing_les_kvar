import json

def change_geometry_type(geometry):
    geom = geometry
    # print(geom)
    # if geom['type'] == 'MULTIPOLYGON':
    #     geom['type'] = 'MultiPolygon'
    # elif geom['type'] == 'POLYGON':
    #     geom['type'] = 'Polygon'
    return geom


def make_feature(value):
    feature = {
        "type": "Feature",
        "properties": { 
            "property 1": value[0],
            "property 2": value[1],
            "property 3": value[2],
            "property 4": value[3],
            "property 5": value[4],
            "kvartal": value[5],
            "property 7": value[6],
            "property 8": value[7],
            "lesnich": value[8],
            "uch_lesnich": value[9],
            },
        # "geometry": change_geometry_type(value[4]),
        "geometry": value[10]
        }
    
    return feature


with open("test.json", "r", encoding="UTF-8") as json_file:
    data = json.load(json_file)
    print(len(data["values"]))

    coords = {
        "type": "FeatureCollection",
        "name": "test_qgis",
        "crs": {"type": "name", "properties": { "name": "urn:ogc:def:crs:EPSG::3857"}},
        "features": [],
    }

    for value in data["values"]:
        coords["features"].append(make_feature(value))

                 
with open('formatted.geojson', 'w', encoding='utf-8') as file:
    json.dump(coords, file)

