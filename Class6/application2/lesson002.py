import csv

csv_file =  'impatient_payments.csv'

with open(csv_file,'rb') as csv_file:
	impatient_dict = csv.DictReader(csv_file,delimiter=",", quotechar='"')
	data = []
	for row in impatient_dict:
		data.append(row)

print
print(data[0].keys())
print("This is the header dictionary version")
raw_input("continue...")

print
for row in data:
	print(row)
print("This is the data dictionary version")
raw_input("continue")

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

print(("zipcode,total cost"))
for zipcd in sorted(max_pay_by_zip.iteritems()):
	print(zipcd)

print("Here are the max values present for each zipcode")
raw_input("continue")

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

print(("zipcode,total cost"))
for zipcd in sorted(min_pay_by_zip.iteritems()):
	print(zipcd)

print("Changing a few signs, we can get minimums")
raw_input("continue")


