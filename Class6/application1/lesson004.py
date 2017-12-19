print("Navigating through and summarizing the metadata")

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

print
print("We bring in data_columns from last exercise...")
print("Note the dictionary comprehension...")
raw_input("continue...")

print(type(json_data['data']))
print
print("Now for the actual data...")
raw_input("continue...")

print(json_data['data'][0])
print
print("We see above it's a list, take one member...")
raw_input('continue...')

print(set([len(datum) for datum in json_data['data']]))
print
print("Do all the data points have the same number of columns.")
raw_input('continue...')

print(len(columns))
print
print("Maybe the columns matches too!")
raw_input('continue...')

column_names = [col['name'] for col in columns]
data_point = json_data['data'][0]
print(zip(column_names,data_point))
print("Let's match up column names with data points:")
raw_input('continue...')

data = {}
for d in json_data['data']:
	for k,v in zip(column_names,d):
		default_key = data.get(k,[])
		default_key.extend([v])
		data[k] = default_key

print(data)
print
print("We now compress the data so each key is associated with a list")
raw_input('continue...')

print(data.keys())
years = list(set(data['Year']))
years.sort()
print
print("year data...")
for year in years:
	print(year)
print
print("This these are the columns...let's choose one...")
raw_input('continue...')

year_counts = {}
for year in data['Year']:
	if year_counts.has_key(year):
		year_counts[year] += 1
	else:
		year_counts[year] = 1


for year, cnt in year_counts.iteritems():
	print(year,cnt)

print
print("This is the count of years...")
raw_input('continue...')

print(len(data['Year']))
print(sum(year_counts.values()))
print(len(data['Year']) == sum(year_counts.values()))
print
print("Let's just do some math!")
print("How many data points does the set have?")
print("What is the sum of the counts!")
raw_input('continue...')

