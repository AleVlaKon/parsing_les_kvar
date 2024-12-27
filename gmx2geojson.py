
import geojson
from collections import OrderedDict


def main(input, output):
    with open(input, 'r', encoding='utf-8') as file:
        source = geojson.load(file)


    # source = geojson.load(input)
    features = list()

    coords = {"name": "test_qgis",
            "crs": { 
                "type": "name", 
                "properties": { 
                    "name": "urn:ogc:def:crs:EPSG::3857" 
                            } 
                    }
            }

    for item in source.get('values'):

        attrs = OrderedDict()
        for idx, ele in enumerate(item):
            if not isinstance(ele, dict):
                key = 'property%s' % (idx, )
                attrs[key] = ele
            else:
                geom = ele
                geom['type'] = (
                    'MultiPolygon' if geom['type'] == 'MULTIPOLYGON' else
                    'Polygon' if geom['type'] == 'POLYGON' else
                    'MultiLineString' if geom['type'] == 'MULTILINESTRING' else
                    'LineString' if geom['type'] == 'LINESTRING' else
                    'MultiPoint' if geom['type'] == 'MULTIPOINT' else
                    'Point' if geom['type'] == 'POINT' else geom['type'])

        feature = geojson.Feature(geometry=geom, properties=attrs)
        features.append(feature)

    collection = geojson.FeatureCollection(features)
    with open(output, 'w', encoding='utf-8') as file:
        geojson.dump(collection, file)
        # geojson.dump(collection, output)


main('test.json', 'formatted.geojson')