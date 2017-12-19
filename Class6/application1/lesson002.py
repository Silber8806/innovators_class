print("How do you navigate a JSON file?")

import json

json_file = 'death.data'

print("reading contents")
contents = open(json_file,'r').read()
json_data = json.loads(contents)

print(json_data)
print
print("We now have a JSON loaded as dictionaries and lists")

raw_input("Continue...")

print
print("Check the first type:")
print(type(json_data))

raw_input("Continue...")

print
print("Dictionaries have keys")
print(json_data.keys())

raw_input("Continue...")

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