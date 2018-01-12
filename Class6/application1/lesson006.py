print("Going through the data structure....")

import json

json_file = 'death.data'
contents = open(json_file,'r').read()
json_data = json.loads(contents)
columns = json_data['meta']['view']['columns'] 
column_names = [col['name'] for col in columns]
data_columns={col["name"]:col for col in columns if col.has_key("tableColumnId")}

data = {}
for d in json_data['data']:
	for k,v in zip(column_names,d):
		default_key = data.get(k,[])
		default_key.extend([v])
		data[k] = default_key

prompt = """
Let's re-use the previous analysis by re-producing both data_columns and data.
data_columns brings in metadata information.  Data brings in the column-based 
version of the data.  We can still loop through json_data['data'] if we want to
access rows.
"""

raw_input(prompt)


for indice, col in zip(range(0,len(column_names)),column_names):
	print(indice, col)

for d in json_data['data'][0:51]:
	print(d[8:])

prompt = """
Before we get deeper into the analysis, we should have a quick overview of the data.
A quick way of accomplishing this is to print the columns (with their positional number)
and 50 or so rows (data points).  We can start making conjecture this way!
"""

raw_input(prompt)

data = {}
for d in json_data['data']:
	for k,v in zip(column_names[8:],d[8:]):
		default_key = data.get(k,[])
		default_key.extend([v])
		data[k] = default_key

prompt = """
Based on the previous overview, we realize that the first 8 columns are not useful.
We decide to limit the data to the last 6 columns for further analysis (conveniently
stored in data).
"""

raw_input(prompt)

unique_values = {k:list(set(v)) for k,v in data.iteritems()}

for k,v in unique_values.iteritems():
	print(k, len(v))

prompt = """
Another technique we can use to get a sense of the data is to go through each column
and list how many unique set of values exist.  Typically data can be divided into
two categories: descriptions and metrics.  Descriptions are "human" categorization
of data.  An example would be states (50 categories).  Metrics on the other hand
are based on measurements or actual counts.  The variation should be larger!
"""

raw_input(prompt)

for k,v in unique_values.iteritems():
	if len(v) < 100:
		print
		print("*****************")
		print("*.   " + k )
		print("*****************")
		v.sort()
		for l in v:
			print l
		print


prompt = """
Let's look at columns with less than 100 unique values.  These are most likely categories.
They also fit the screen better and can be seen at a glance.
"""

raw_input(prompt)

print
print("Let's pick 3 valeus for State, Cause and Year....")

print
print("State:")
print("United States")

print
print("Cause Name:")
print("All Causes")

print
print("Year:")
print("2015")

print
for d in json_data['data']:
	row = d[8:]
	year, cause, state, deaths = row[0],row[2],row[3], row[-2]
	if (year == "2015" and cause == "All Causes" and state == "United States"):
		print("How many deaths in total in the US:")
		print(deaths)

print("We can also analyze this by year!")
raw_input("continue...")

print
print("Let's define some filters....")

print
print("State:")
print("United States")

print
print("Cause Name:")
print("All Causes")

print
print("By Year:")
total = 0
for d in json_data['data']:
	row = d[8:]
	year, cause, state, deaths = row[0], row[2],row[3], row[-2]
	if (cause == "All Causes" and state == "United States"):
		print(str(year) + ": " +  str(deaths))
		total += int(deaths)

print
print("Yearly summaries:")
print("Total above for 17 years is: %s" % total)
print("Average is: " + str(total/17))
raw_input("continue...")


print
year_total_deaths={}
cancer_total_deaths={}
for d in json_data['data']:
	row = d[8:]
	year, cause, state, deaths = row[0], row[2],row[3], row[-2]
	if (cause == "All Causes" and state == "United States"):
		year_total_deaths[year] = deaths
	if (cause == "Cancer" and state == "United States"):
		cancer_total_deaths[year] = deaths

print("year totals by year:")
print(year_total_deaths)
print("cancer totals by year:")
print(cancer_total_deaths)
print

prompt = """
Let's do something a bit more interesting!  Wouldn't it be cool
to find out what percent of deaths are cancer related!

To do this, we first need to get the total deaths by year.

Then, we need to get total cancer deaths by years.

We can than divide: "cancer deaths" / "total deaths"

Before we can do that, we need to test some assumptions!

"""

raw_input(prompt)

unique_years = set(year_total_deaths.keys())
unique_cancers = set(cancer_total_deaths.keys())

print
if(len(unique_cancers.symmetric_difference(unique_years)) == 0):
	print("No")
else:
	print("Yes")

prompt = """
We need to make sure that every year in death totals has a data
point in cancer deaths.  If one of the years is missing, we 
will have to handle the "bad" data.  Luckily, the data is complete.
Every year is present in both total deaths and cancer deaths!
"""

raw_input(prompt)


cancer_table = []
for year in unique_years:
	total_death = year_total_deaths[year]
	cancer_death = cancer_total_deaths[year]
	year, cancer_death, total_death= int(year), int(cancer_death), int(total_death)
	cancer_rate = round(100 * cancer_death / float(total_death),2)
	cancer_table.append([year, cancer_death,total_death,cancer_rate])

cancer_table.sort(key=lambda x: x[0])

print
print ("year,cancer,total,percent".split(","))
for row in cancer_table:
	print(row)

prompt = """
We finally produce summarized output for cancer death rates.
The final "table" called cancer table has 4 columns:

year
total deaths
cancer deaths
cancer rate

We can now ask questions about cancer rate by year!
"""

raw_input(prompt)

cancer_table.append([1998,500000,2500000,20.00])
cancer_table.append([2018,600000,2700000,22.22])
json.dumps(cancer_table,indent=4)

cancer_table.sort(key=lambda x: x[0])

print
print ("year,cancer,total,percent".split(","))
for row in cancer_table:
	print(row)


prompt = """
Now a good question?  What if we wanted to add 
two new data points we just found out about.
Let's say data came in for 1998 and 2018:

[1998,500000,2500000,20.00]
[2018,600000,2700000,22.22]

We can just append this to the cancer table
and quickly filter by year!
"""

raw_input(prompt)

tree_top = {}
tree_top["yearly"] = {}
tree_top["yearly"]["data"] = cancer_table

print(json.dumps(tree_top, indent=4))

prompt = """
Let's create our own json file.  Let's call
it cancer.json and have it contain our 
cancer table as data points.

The first step is to create a top-level dict.

We can than add dictionaries to it to describe
the hierarcy.  In the above case, one hierarchy
is:

	"yearly" => "data" => <cancer table>

Let's add some extra information!
"""

raw_input(prompt)

meta = ["year","cancer_death","total_death","percent"]
tree_top["yearly"]["meta"] = meta

print(json.dumps(tree_top, indent=4))

prompt = """
One thing that might be valuable is metadata.
Let's put the column names in meta.

	"yearly" => "meta" => <column names>

I think this makes for a great cancer.json document
that can be used by us or others.
"""

raw_input(prompt)

to_json = open('cancer.json','w')
to_json.write(json.dumps(tree_top, indent=4))
to_json.close()

from_json = open('cancer.json','r')
json_contents = from_json.read()
print(json_contents)

prompt = """
Let's finally write the file to disk for more 
permanent storage (disk instead of memory). 
Let's call it cancer.json.

To confirm this, we can read the contents 
of the file and print them to the screen.
"""

raw_input(prompt)




