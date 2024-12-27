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
            "kvartal": value[0],
            "lesnich": value[1],
            "uch_lesnich": value[2],
            "fond": value[3]},
        # "geometry": change_geometry_type(value[4]),
        "geometry": value[4]
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