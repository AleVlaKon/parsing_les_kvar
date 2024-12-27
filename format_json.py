import json
import requests


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
        "geometry": value[11]
        }
    return feature


def get_dict_data_from_url(url: str) -> dict:
    data_text = requests.get(url)
    return json.loads(data_text.text[27:-1])


def get_dict_data_from_file(filename: str) -> dict:
    with open(filename, "r", encoding="UTF-8") as json_file:
        data = json.load(json_file)
        return data


def collect_features(sourses:list) -> list:
    features = []
    for url in sourses:
        try:
            data = get_dict_data_from_url(url)
            for value in data["values"]:
                    features.append(make_feature(value))
        except:
            print('Ошибочный URL')
    return features


def make_geojson(sourses:list):
    coords = {
        "type": "FeatureCollection",
        "name": "test_qgis",
        "crs": {"type": "name", "properties": { "name": "urn:ogc:def:crs:EPSG::3857"}},
        "features": collect_features(sourses),
    }

    with open('formatted.geojson', 'w', encoding='utf-8') as file:
        json.dump(coords, file)


with open('urls.txt', encoding='utf-8') as file:
    sourses = file.readlines()

make_geojson(sourses)