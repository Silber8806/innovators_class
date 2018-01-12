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

prompt = """
cancer.json is not useful on our computer.  It would
be much better to have it accessible via the internet.

We can use the SimpleHTTPServer to demonstrate how
JSON is used to pass data across the web.

to begin SimpleHTTPServer type (commandline/terminal):

	python -m SimpleHTTPServer

Make sure you are in the same directory as the 
json file.

After setting this up, we can use the requests library,
a special library in python for making "browser" 
like connections to servers and retreiving data.

	requests.get(url) => retrieves data from the url

Whenever we make a web connection, we have to test if
it succeeded.  To do that, we have to check it's status
code:
	
	<request>.status_code

200 means success, 404 means page not found, 500 is a server
error and 402 means you don't have a login!

Once you have a successful request (200), you can get it's
content using:

	r.content.

This should retrieve the json file.  Note if the SimpleHTTPServer
is not running or the file is missing.  It will fail.
"""

raw_input(prompt)


json_data = json.loads(r.content)
meta = json_data['yearly']['meta']
print(meta)

data = json_data['yearly']['data']
print(data)

prompt = """
We can confirm JSON is cancer.json
by printing:
	
	json_data['yearly']['data']
	json_data['yearly']['meta']

You'll notice the structure we set up!
"""

raw_input(prompt)

print
print(meta)
for row in data:
	print row

prompt = """
We can reconstruct our cancer.json table from
the new json object!
"""

raw_input(prompt)
