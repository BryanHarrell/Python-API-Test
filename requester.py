import requests
import json
from pprint import pprint
headers = {'User-Agent': 'MyCoolTool/1.1 (http://example.com/MyCoolTool/; bryan@lifeofbrybry.com)'}
payload = {'format': 'json', 'action': 'query', 'titles': 'Main Page', 'continue': "", 'prop': 'revisions', 'rvprop': 'content'}
r = requests.get('http://en.wikipedia.org/w/api.php', params=payload, headers=headers)
response = r.json()
#pprint(response)
print (response['query'])
