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
After looking at metadata, we should have some idea about the columns in the data
set.  We also prepared the 'data columns' dictionary for looking up information
and adding formatting to later data outputs.

The next thing we should do is dig into the 'data' key at the root-level!  When
checking the type this time, we find that it is a <list> type.  Often, large 
collections of objects like data points are stored in list format.
"""

raw_input(prompt)

print(json_data['data'][0])

prompt = """
When we have a list as root: json_data['data'], it is often worth looking at 
a single data point.  We can do this using:

json_data['data'][0]

Looking at the data point, we can start making some assumptions about the remaining
items.  In this case, it seems that all data points are stored within the 
json_data['data'] key. I now test my assumption!
"""

raw_input(prompt)

print(set([len(datum) for datum in json_data['data']]))
prompt = """
A common 'sanity' test is to count all the columns of each row.  To do this, we 
first loop through each member of the json_data['data'] collection and take it's
len.  We than use the 'set' command to see if there are different numbers of 
columns for any of the points.  If we find multiple numbers in the set,
we might want to explore a few data points with different column lengths to 
see how they differ.  In this case, all the data points have the same column
length.  It's possible that only data points are stored under json_data['data'].
"""

raw_input(prompt)

print(len(columns))
prompt = """
If json_data['data'] is only data points, a good second 'sanity' test would be 
to count the number of columns in 'meta' and compare it with the columns within
these data points.  If they are the same, there is a good change that the 
'meta' data describes the columns within 'data'.  We take the length of 'meta'
data columns.  It is the same.  
"""

raw_input(prompt)

column_names = [col['name'] for col in columns]
data_point = json_data['data'][0]
print(zip(column_names,data_point))
prompt = """
Having confirmed that the data points have 14 columns and the metadata shows
14 column descriptions, it's worth testing the assumption that both are in
order.  That is to say, the first column in meta is the 0th index of the data
point.  The second column is the 1st index of the data point.  We can do this
with the zip command.
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
We've now confirmed that the data points are all most likely under json_data['data'].
I decide to explore each column for unique values.  To do this, I create a dictionary
called data.  I use the column names from the meta_data as the key.  I use the columns
of the data points to populate a list (associated with the key).

Once this is done, the data "dictionary" will contain a key for each column and all
the values within each column.
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
We can now retrieve the entire "Year" column using data['Year'].  If we
wanted to list all years in ascending order, we can retrieve all years,
use a set to remove duplicates, convert it back to a list and then sort it.
This is what happens in the above code!
"""

raw_input(prompt)

year_counts = {}
for year in data['Year']:
	if year_counts.has_key(year):
		year_counts[year] += 1
	else:
		year_counts[year] = 1


for year, cnt in sorted(year_counts.iteritems()):
	print(year,cnt)

prompt = """
Let's say we wanted to know the actual count of each year.  We can use a 
dictionary called year_counts.  year_counts[<year>] starts at 1 when it
first encounters <year>.  It then increments by 1 for each subsequent
encounter.

We print a sorted version of year counts after tallying the counts.  
This works, because <dict>.iteritems() produces a list of tuples.
By default, if year is the key (year, count), it shows up first
and is the first thing to be sorted.
"""

raw_input(prompt)

print(len(data['Year']))
print(sum(year_counts.values()))
print(len(data['Year']) == sum(year_counts.values()))

prompt = """
We can do one last sanity check.  The sum of the yearly counts. Should
be the same as the number of entries in a column.  In this case, 
it is true!
"""

raw_input(prompt)


