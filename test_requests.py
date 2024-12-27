import requests
import json


url = 'https://maps.kosmosnimki.ru/TileSender.ashx?WrapStyle=None&key=Cd0juhhxtAZS60jAnID0UGhIYzdqLPTVlcO2+3WQXJkQuCKE9Q9guoLlM+jpnxIG1QlNSMIjfXKElb7+JqpHHs1PWlt7vy1gJ7TlX4zDzUE=&ModeKey=tile&ftc=osm&r=j&LayerName=7765932DD6A84F7BA31CED9A28764033&z=9&x=303&y=145&v=0&srs=3857&sw=1'

data = requests.get(url)

print(data.text[28:-1])
print(json.loads(data.text[27:-1]))

