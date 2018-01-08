import csv

csv_file =  'impatient_payments.csv'

with open(csv_file,'rb') as csv_file:
	impatient_dict = csv.DictReader(csv_file,delimiter=",", quotechar='"')
	data = []
	for row in impatient_dict:
		data.append(row)

prompt="""
We start this session by importing select logic from lesson012.py.
"""

raw_input(prompt)

zipcode_key = 'Provider Zip Code'
total_pay_key = ' Average Total Payments '

max_pay_by_zip = {}

print
for row in data:
	zipcode = row[zipcode_key]
	total_pay = float(row[total_pay_key].replace("$",""))
	if (max_pay_by_zip.has_key(zipcode)):
		current_pay = max_pay_by_zip[zipcode]
		if (total_pay > current_pay):
			max_pay_by_zip[zipcode] =  total_pay
	else:
		max_pay_by_zip[zipcode] = total_pay

prompt="""
Let's say that I want to look at only zip code and average total pay.
This time, I would like a list of minimum and low payments.  How
would I get around this?
"""

raw_input(prompt)


print(("zipcode,total cost"))
for zipcd in sorted(max_pay_by_zip.iteritems()):
	print(zipcd)

prompt="""
We can see in the above, that the logic does produce maximum payments
by zipcode.
"""

raw_input(prompt)

min_pay_by_zip = {}

print
for row in data:
	zipcode = row[zipcode_key]
	total_pay = float(row[total_pay_key].replace("$",""))
	if (min_pay_by_zip.has_key(zipcode)):
		current_pay = min_pay_by_zip[zipcode]
		if (total_pay < current_pay):
			min_pay_by_zip[zipcode] =  total_pay
	else:
		min_pay_by_zip[zipcode] = total_pay

prompt="""
We can change a simple sign to get minimum payments!
"""

raw_input(prompt)

print(("zipcode,total cost"))
for zipcd in sorted(min_pay_by_zip.iteritems()):
	print(zipcd)

prompt="""
The above shows you the minimum payments...
"""

raw_input(prompt)


range_pay_by_zip = {}

print
for row in data:
	zipcode = row[zipcode_key]
	total_pay = float(row[total_pay_key].replace("$",""))
	if (range_pay_by_zip.has_key(zipcode)):
		min_pay = range_pay_by_zip[zipcode][0]
		max_pay = range_pay_by_zip[zipcode][1]
		if (total_pay < min_pay):
			range_pay_by_zip[zipcode][0] =  total_pay
		if (total_pay > max_pay):
			range_pay_by_zip[zipcode][1] =  total_pay
	else:
		range_pay_by_zip[zipcode] = [total_pay,total_pay]


prompt="""
We can even make a few changes to create a range...
"""

raw_input(prompt)

print(("zipcode,total cost"))
for zipcd in sorted(range_pay_by_zip.iteritems()):
	print(zipcd)

prompt="""
The above shows you the minimum payments...
"""

raw_input(prompt)

