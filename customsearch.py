import requests
import json
from pprint import pprint
payload = {'key': 'AIzaSyDPkEcWi_otlQq87wuBivchhSw8kwKyr_M', 'cx':'008743726290765473151:u8xj-02hvbc','q':'science'}
r = requests.get('https://www.googleapis.com/customsearch/v1', params=payload)
response = r.json()
#pprint(response)
pprint(response['items'][0]['pagemap']['metatags'][0]['og:description'])
