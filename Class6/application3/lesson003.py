import csv
import sys

csv_file =  'impatient_payments.csv'

with open(csv_file,'rb') as csv_file:
	impatient_data = csv.reader(csv_file,delimiter=",", quotechar='"')
	header = impatient_data.next()
	data = []
	for row in impatient_data:
		data.append(row)

prompt="""
We start this session by importing the data and header logic from lesson001.py.
We begin by filtering out only data that interests us and doing some basic 
data cleaning.
"""

raw_input(prompt)

print(header)
for row in data[0:11]:
	print row

prompt="""
Before we can analyze data we need to start with som basic assumptions.  To do that
it's best to look at a small subset of data to see what we are dealing with!
"""

raw_input(prompt)

columns_of_interest=['DRG Definition','Provider State',' Average Total Payments ']

column_indices = [header.index(col) for col in columns_of_interest]
interesting_data = []

for row in data:
	temp_data = []
	for i in column_indices:
		temp_data.extend([row[i]])
	interesting_data.append(temp_data)

full_data = data
data = interesting_data

prompt="""
Looking at the data, I can conclude that this data represents:

Diagnosis combined with Area and lists the average: total payment, medicare payment 
and covered charge.  

We could find out expensive places to live in terms of charge codes from this data
or possibly find out the most expensive procedures.

Since most columns provide a "reindentification" of Diagnosis or Location, let's 
pick 2 specific values to represent it:

DRG Definition - Looks like a diagnosis with a code included.
Provider State - The hospital location as a state.
Average Total Payments - Dollar value of care for the state + procedure

Let's use lists, dictionaries and comprehensions to limit our data to that set.
"""

raw_input(prompt)

prompt="""
We can now look at the subset of data to see if we properly filtered.
We should regularly test data analysis code to make sure our assumptions 
hold.
"""

print(columns_of_interest)
for row in data[0:11]:
	print(row)

raw_input(prompt)

prompt="""
One problem with CSV reader is that it converts those values with $
into strings.  We will have to strip those values from out data
and then convert them into floats.  Since it's dollar valued, we 
have to roudn to 2 decimal places.  This is a typical data 
cleaning process.
"""

for row in data:
	row[2] = round(float(row[2].replace("$","")),2)

for row in data[0:11]:
	print(row)

raw_input(prompt)

sys.exit(0)