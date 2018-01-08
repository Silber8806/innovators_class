# run python -m SimpleHTTPServer 

import requests
import sys
import json

local_url='http://127.0.0.1:8000/cancer.json'

r = requests.get(local_url)

if (r.status_code == 200):
	print("status code is: %s" % r.status_code)
else:
	sys.exit(1)


print(r.content)
print("After running SimpleHTTPServer we can retrieve")
print("The JSON from the web locally.")
raw_input("continue...")


json_data = json.loads(r.content)
meta = json_data['yearly']['meta']
print(meta)

print
print("After running SimpleHTTPServer we can retrieve")
print("The JSON from the web locally.")
print("Notice how we retrieved meta....")
raw_input("continue...")

data = json_data['yearly']['data']
print(data)

print
print("We can also retrieve data portion")
raw_input("continue...")

print
print(meta)
for row in data:
	print row

print
print("We can recreate the table just as previously dones..")
raw_input("continue...")
