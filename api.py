import requests
import json
# response_API = requests.get('https://api.covid19india.org/state_district_wise.json')
response_API = requests.get('https://jsonplaceholder.typicode.com/todos/1')
# print(response_API.status_code)
# print(response_API.text)
data = response_API.text
parse_json = json.loads(data)
print(parse_json)