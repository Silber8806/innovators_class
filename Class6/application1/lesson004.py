import json

json_file = 'death.data'

print("reading contents")
contents = open(json_file,'r').read()
json_data = json.loads(contents)

prompt = """
We borrow code from lesson003.py.
We will investigate only the metadata
portion of the data this time!
"""

raw_input(prompt)

print(json.dumps(json_data['meta'],indent=4))

prompt = """
Typically when I see a metadata portion of data
I'm interested in it.  It provides you some
sense of what is present.  It can also hint 
at caveats or measurements.

We can use the json.dumps(<dict/list>, indent=<int>)

to print a subsection (meta) of the json object in 
json format.

This is useful for eye-balling the data and 
getting a sense of it's structure and content.
"""

raw_input(prompt)

meta = json_data['meta']
print(meta.keys())

prompt = """
We can look at the keys at the:

	root > meta

branch to see what else is available:
"""

raw_input(prompt)

print(meta['view'].keys())

prompt = """
We can keep descendign the data structure!

	root > meta > view

When we go down meta, we see view.  View
seems to have information about columns!
"""

raw_input(prompt)

print(json.dumps(meta['view']['columns'],indent=4))

prompt = """
We get to columns:

	root > meta > view > columns

To get a better view of columns, I can use the 
json.dumps command to see it in JSON format!
"""

raw_input(prompt)

columns = meta['view']['columns']

for col in columns:
	print
	print(col)
	print

prompt = """
The JSON seems to indicate a list 
of dictionaries.  Each dictionary being
a column with properties.  Let's use a for
loop to compare values between columns!
"""

raw_input(prompt)

for col in columns:
	if col.has_key("tableColumnId"):
		print
		print(col['name'])
		print
		print(col)
		print

prompt = """
Looking at the data, I see a lot of 
columns with hidden flag.  It seems that
legitimate columns contain a field called:

tableColumnId
"""

raw_input(prompt)

for col in columns:
	if col.has_key("tableColumnId"):
		if col['name'] == "Deaths":
			print(json.dumps(col,indent=4))

prompt = """
Let's "zoom" in on a single column.

Deaths seems interesting.

We can use json.dumps again for 
eye-balling purposes.
"""

raw_input(prompt)

data_columns = []
for col in columns:
	if col.has_key("tableColumnId"):
		data_columns.append(col["name"])

print(data_columns)
prompt = """
Let's get a list of all columns!
We can filter to columns by 
checking for a tableColumnId.  

We can then append the name to data_columns
list.
"""

raw_input(prompt)

data_columns = {}
for col in columns:
	if col.has_key("tableColumnId"):
		data_columns[col["name"]]=col

print(data_columns)
prompt = """
If we wanted to store the attributes of the columns
by name, it might be worth storing this information
in a dictionary.

name = <column json>

This would make it easier to look things up on 
demand, while doing analysis.
"""
raw_input(prompt)

for col in data_columns.keys():
	print(col)

prompt = """
We can still look up column names through the
dict.keys() methods.

I think this is better!  Let's start looking at
the actual data in the next section!
"""
raw_input(prompt)


