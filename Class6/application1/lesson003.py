import json

json_file = 'death.data'
contents = open(json_file,'r').read()

prompt = """
Borrow code from lesson002.py.  Read the contents
of the JSON file into the content variable.
"""

raw_input(prompt)

json_data = json.loads(contents)

print(json_data)

prompt = """
Python can treat a json file as 
a set of dictionaries and lists.
To do so, you have to first import
the json library:

	import json

then you can use:

	json.loads(<json_string_data>)

to turn the JSON string into python
dictionaries and lists.  

The downside of json.loads is that
it becomes harder to read when 
printed!  See above!
"""

raw_input(prompt)

print(type(json_data))

prompt = """
json.loads returns either a 
dictionary or list.  We use
print(type(json_data)).

In this case, json_data is 
a dictionary!
"""

raw_input(prompt)

print(json_data.keys())

prompt = """
A dictionary has keys!  In this 
case it is meta and data.  In 
data community, meta typically 
refers to metadata.  data refers
to ... data.  

Press ENTER to learn more about the
terms: 
...
"""

raw_input(prompt)

print
print(
	"""
	metadata is data about the data.
	you can think about it as the header
	of a CSV file. 
	""")

raw_input("Continue...")

print
print(
	"""
	data is the actual data.  Note this data is
	present with limited information about it.  
	Use the metadata to understand what the data
	is about!
	"""
	)

raw_input("Continue...")