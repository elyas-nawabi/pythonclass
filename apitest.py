# API: acronym , application programming interface
# as a composition of rules that enables us to access an external
# service on web through our systems
# an API is considered as a data source available on web which  can 
# can be accessed through particular libraries.
# website: mustafa.com    --> weather, news
#  request 
# get command
#  post command
#  delete command, put command

# response
# 200 ok
# 204: 
# 401 :
# 403 
# 404
# 505
# 
# pip install requests 
import requests
response_api = requests.get('https://jsonplaceholder.typicode.com/photos/1')
# print(response_api.status_code)
# pull data from an api in python
data = response_api.text
print(data)
