import csv

csv_file =  'impatient_payments.csv'

with open(csv_file,'rb') as csv_file:
	impatient_dict = csv.DictReader(csv_file,delimiter=",", quotechar='"')
	data = []
	for row in impatient_dict:
		data.append(row)

prompt="""
We saw how we could read and manipulate the csv file as a set of lists.
What about using the dictionary varient.

The only difference in this case is that we use:

csv.DictReader

instead of:

csv.Reader

The result will turn the rows into dictionaries instead of lists.
Let's see the header and data:
"""

raw_input(prompt)

print(data[0].keys())

prompt="""
The header in this case can be obtained from any row.
It represents just the dictionary keys of a single 
data point.
"""

raw_input(prompt)

print
for row in data:
	print(row)

prompt="""
What about the actual data.  We can loop through the 
data variable to see that they are now all dictionaries...
"""

