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

print
print("We start with data, data_columns from previous examples")
raw_input("continue...")

for indice, col in zip(range(0,len(column_names)),column_names):
	print(indice, col)

for d in json_data['data'][0:51]:
	print(d[8:])

print
print("Let's look at the first 50 columns...")
raw_input("continue...")

data = {}
for d in json_data['data']:
	for k,v in zip(column_names[8:],d[8:]):
		default_key = data.get(k,[])
		default_key.extend([v])
		data[k] = default_key

print
print("Take only the 6 and further columns for data....")
raw_input("continue...")

unique_values = {k:list(set(v)) for k,v in data.iteritems()}

for k,v in unique_values.iteritems():
	print(k, len(v))

print("What's the unique count of each type of item?")
raw_input("continue...")

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


print("Let's look at those with only 100 or less unique values...?")
print("Anything more is most likely a number....")
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
print("Year:")
print("2015")

print
for d in json_data['data']:
	row = d[8:]
	year, cause, state, deaths = row[0],row[2],row[3], row[-2]
	if (year == "2015" and cause == "All Causes" and state == "United States"):
		print("How many deaths in total in the US:")
		print(deaths)

print("Let's see what we get!")
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
raw_input("continue...")

unique_years = set(year_total_deaths.keys())
unique_cancers = set(cancer_total_deaths.keys())

print
if(len(unique_cancers.symmetric_difference(unique_years)) == 0):
	print("No")
else:
	print("Yes")

print("Are there any years missing?")
raw_input("continue...")

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

print("Let's see the cancer rate by table:")
raw_input("continue...")

cancer_table.append([1998,500000,2500000,20.00])
cancer_table.append([2018,600000,2700000,22.22])
json.dumps(cancer_table,indent=4)

cancer_table.sort(key=lambda x: x[0])

print
print ("year,cancer,total,percent".split(","))
for row in cancer_table:
	print(row)

print("Let's add a 2 rows to the cancer table...")
raw_input("continue...")

tree_top = {}
tree_top["yearly"] = {}
tree_top["yearly"]["data"] = cancer_table

print(json.dumps(tree_top, indent=4))

print("Let's make our own json...")
raw_input("continue...")

meta = ["year","cancer_death","total_death","percent"]
tree_top["yearly"]["meta"] = meta

print(json.dumps(tree_top, indent=4))

print("We can make our own meta data too!")
raw_input("continue...")

to_json = open('cancer.json','w')
to_json.write(json.dumps(tree_top, indent=4))
to_json.close()

from_json = open('cancer.json','r')
json_contents = from_json.read()
print(json_contents)

print("Let's write to a file and then open it!")
raw_input("continue...")



