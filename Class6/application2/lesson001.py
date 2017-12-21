import csv

csv_file =  'impatient_payments.csv'

with open(csv_file,'rb') as csv_file:
	impatient_data = csv.reader(csv_file,delimiter=",", quotechar='"')
	header = impatient_data.next()
	data = []
	for row in impatient_data:
		data.append(row)

print
print(header)
print("This is the header")
raw_input("continue...")

print
for row in data:
	print(row)
print("This is the data")
raw_input("continue")

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

print
print(columns_of_interest)
for row in data[0:11]:
	print(row)

print("Let's subset the data...")
print("I only took 3 columns: %s" % columns_of_interest)
raw_input("continue...")

for row in data:
	row[2] = round(float(row[2].replace("$","")),2)

print
for row in data[0:11]:
	print(row)
print("Let's clean up the dollar sign for average cost!")
raw_input("continue...")

diagnosis = set()
state = set()

for row in data:
	if row[0] not in diagnosis:
		diagnosis.add(row[0])
	if row[1] not in state:
		state.add(row[1])

diagnosis={d:[] for d in list(diagnosis)}
state={s:[] for s in list(state)}
combos = {s + '|' + d:[] for d in list(diagnosis) for s in list(state)}

print(combos)
print
print("Let's get all unique combos of state, diagnois and state-diagnosis!")
raw_input("continue...")

combos.update(state)
combos.update(diagnosis)

for row in data:
	charge = row[2]
	combos[row[1] + '|' + row[0]].extend([charge])
	combos[row[0]].extend([charge])
	combos[row[1]].extend([charge])

print(combos)
print
print("We can get all the data in one giant dictionary!")
raw_input("continue...")

for k,v in combos.iteritems():
	total = sum(v)
	members = len(v)
	if ( members == 0 ):
		total = 0
		members = 1
	combos[k] = round(total/float(members),2)

combo_list = [[k,v] for k,v in combos.iteritems()]
combo_list.sort(key=lambda x: x[0])

for row in combo_list:
	print(row)

print
print("Above we have the average value of all services...")
print("By all possible combinations of keys...")
raw_input("continue")

print
print("average service cost for New York!")
print(combos['NY'])

print
print("average service cost for '948 - SIGNS & SYMPTOMS W/O MCC'")
print(combos['948 - SIGNS & SYMPTOMS W/O MCC'])

print
print("average service cost for '948 - SIGNS & SYMPTOMS W/O MCC' in New York")
print(combos['NY|948 - SIGNS & SYMPTOMS W/O MCC'])

print
print("We can use the dictionary to retrive specific cases")
raw_input("continue")



