import json

json_file = 'death.data'
contents = open(json_file,'r').read()
json_data = json.loads(contents)
columns = json_data['meta']['view']['columns'] 

data_columns={col["name"]:col for col in columns if col.has_key("tableColumnId")}

for k,v in data_columns.iteritems():
	print
	print(k,v)
	print

prompt = """
I use a shortcut to recreate the data from lesson004.py.  A dictionary of columns
with their associated properties in JSON format.
"""

raw_input(prompt)


print(type(json_data['data']))

prompt = """
Alright, let's look at the data object by
checking it's root level!

It seems to be a list of data points, which
would make it easy to traverse!
"""

raw_input(prompt)

print(json_data['data'][0])

prompt = """
Let's look at a single data point!
"""

raw_input(prompt)

print(set([len(datum) for datum in json_data['data']]))
prompt = """
If it has the same number of columns for each data 
point, then I can access everything through a single 
index.

Here I test if the lengths vary by data point!

In this case, they all have the same length.
"""

raw_input(prompt)

print(len(columns))
prompt = """
Does it match with the metadata column length?

It does, it's probably a one-to-one match!
"""

raw_input(prompt)

column_names = [col['name'] for col in columns]
data_point = json_data['data'][0]
print(zip(column_names,data_point))
prompt = """
We can match up the column name from our metadata
analysis with the single data point.

Do the columns make sense relative to the data?

I think so!
"""

raw_input(prompt)

data = {}
for d in json_data['data']:
	for k,v in zip(column_names,d):
		default_key = data.get(k,[])
		default_key.extend([v])
		data[k] = default_key

print(data)
prompt = """
We can get a list of all values in a column by
adding it to a dictionary of lists!
"""

raw_input(prompt)

print(data.keys())
years = list(set(data['Year']))
years.sort()
print
print("year data...")
for year in years:
	print(year)
print

prompt = """
We can get a list of years by looking up the
Year in our new dictionary.  We use set to 
create a unique set.

We convert it to a list so that we can sort it
making it easier to interpret for people!
"""

raw_input(prompt)

year_counts = {}
for year in data['Year']:
	if year_counts.has_key(year):
		year_counts[year] += 1
	else:
		year_counts[year] = 1


for year, cnt in year_counts.iteritems():
	print(year,cnt)

prompt = """
The last example uses a dictionary to count
the number of records per year!
"""

raw_input(prompt)

print(len(data['Year']))
print(sum(year_counts.values()))
print(len(data['Year']) == sum(year_counts.values()))

prompt = """
We can get the number of records in years to get 
the total number of data points!

We can then use the dict.values() method to retrieve 
the counts by year and sum them.

Are they the same value?

Yes!

It's always worth doing these little sanity tests!
"""

raw_input(prompt)


