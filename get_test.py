import requests
import json
from flask import jsonify

url = 'http://127.0.0.1:6010/completions'
headers = {'Content-Type': 'application/json'}

filters = {'prompt':'LinkedIn is a great company2 LinkedIn is a great company2 '}
#print(jsonify(filters))
#params = dict(json=json.dumps(filters))
print(filters)
print(json.dumps(filters))
response = requests.post(url, json=filters,headers=headers)
#print(response.text)
assert response.status_code == 200
print(response.json()['choices'][0]['text'])
print(len(response.json()['choices']))

exit()

import requests

url = 'http://127.0.0.1:6010'
#url = 'https://httpbin.org/post'

# POST/form data
payload = {
    'search': 'hello world',
}

r = requests.post(url, data=payload)

print(r.text)
