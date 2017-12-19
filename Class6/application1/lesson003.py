print("Finding the column metadata...")

import json

json_file = 'death.data'

print("reading contents")
contents = open(json_file,'r').read()
json_data = json.loads(contents)

print(json.dumps(json_data['meta'],indent=4))
print
print("Let's look at the metadata above!")
raw_input("Continue...")

meta = json_data['meta']
print(meta.keys())
print
print("meta keys:")
raw_input("Continue...")

print(meta['view'].keys())
print
print("meta.view keys")
raw_input("Continue...")

print(json.dumps(meta['view']['columns'],indent=4))
print
print("meta.view.columns -> probably the columns!")
raw_input("Continue...")

columns = meta['view']['columns']

for col in columns:
	print
	print(col)
	print

print
print("Looking at this data, I see hidden flags")
raw_input("Continue...")

for col in columns:
	if col.has_key("tableColumnId"):
		print
		print(col['name'])
		print
		print(col)
		print

print("Looking at this data, I see hidden flags")
print("tableColumnId seems to be legit data...")
raw_input("Continue...")

for col in columns:
	if col.has_key("tableColumnId"):
		if col['name'] == "Deaths":
			print(json.dumps(col,indent=4))

print("This is a single column and all associated data...")
print("The cached contents looks interesting...it gives...")
print("averages,small and large values...")
raw_input("Continue....")

data_columns = []
for col in columns:
	if col.has_key("tableColumnId"):
		data_columns.append(col["name"])

print(data_columns)
print
print("Let's get a list of all columns...")
raw_input("Continue....")

data_columns = {}
for col in columns:
	if col.has_key("tableColumnId"):
		data_columns[col["name"]]=col

print(data_columns)
print
print("Maybe a dictionary of columns would be more userful")
raw_input("Continue...")

for col in data_columns.keys():
	print(col)
print
print("Now we can get the columns on demand...")
raw_input("Continue...")



