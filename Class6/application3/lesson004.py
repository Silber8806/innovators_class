import csv

csv_file =  'impatient_payments.csv'

with open(csv_file,'rb') as csv_file:
	impatient_data = csv.reader(csv_file,delimiter=",", quotechar='"')
	header = impatient_data.next()
	data = []
	for row in impatient_data:
		data.append(row)

columns_of_interest=['DRG Definition','Provider State',' Average Total Payments ']
column_indices = [header.index(col) for col in columns_of_interest]
interesting_data = []

for row in data:
	temp_data = []
	for i in column_indices:
		temp_data.extend([row[i]])
	interesting_data.append(temp_data)

data = interesting_data

for row in data:
	row[2] = round(float(row[2].replace("$","")),2)

prompt="""
We start this session by importing select logic from lesson002.py.
In this lecture, we use a combination of dicts, lists and sets
to create a dicationary of all state, diagnosis and state|diagnosis
combinations.  We then find the average payment for each...
"""

raw_input(prompt)

diagnosis = set()
state = set()

for row in data:
	if row[0] not in diagnosis:
		diagnosis.add(row[0])
	if row[1] not in state:
		state.add(row[1])

prompt="""
The first thing we need to do is loop through the data and find all unique
diagnosis and state values.  We add them to two sets to make sure we retrieve
only the unique values.

Once we have the unique values, we can convert them to dictionaries.  We can
also combine both sets to create all combos: <state>|<diagnosis>.  
"""

raw_input(prompt)

diagnosis={d:[] for d in list(diagnosis)}
state={s:[] for s in list(state)}
combos = {s + '|' + d:[] for d in list(diagnosis) for s in list(state)}

prompt="""
Once we have unique sets of states and diagnosis.  We can convert them to 
dictionaires with dictionary comprehension.  

We can also create a combination of all diagnosis/states this way.  This
is done with "combos" variable.

We have each member of the dictionary associated with a blank list.
We will add all related "charges" to the list depending on their
state and diagnosis code...
"""

raw_input(prompt)

combos.update(state)
combos.update(diagnosis)

prompt="""
update let's us combine the states and diagnosis dictionaries 
with their combined states.  All states will be present in
the combos variable.  We will print this below:
"""

raw_input(prompt)

prompt="""
All possible states and diagnosis codes:
"""
print(combos)
raw_input(prompt)

for row in data:
	charge = row[2]
	combos[row[1] + '|' + row[0]].extend([charge])
	combos[row[0]].extend([charge])
	combos[row[1]].extend([charge])

prompt="""
We can finally associated each average total payment with
it's state, diagnosis code and combined <state>|<diagnosis> code.

We will do this so that we can get the average per:

State
Diagnosis Code
State and Diagnosis Code combination

"""

raw_input(prompt)

for k,v in combos.iteritems():
	total = sum(v)
	members = len(v)
	if ( members == 0 ):
		total = 0
		members = 1
	combos[k] = round(total/float(members),2)


prompt="""
For each category, we want to:

	average total payment = sum of total payments / number of total payments

To do this, we go through the dictionary member by member.  We 
retrieve the list associated with each key, which contains
all charges.

We then sum the list to get a sum of total payments.
We get the lenght of the list to get total number of payments.

We then divide: total/members.

We have 1 exception in this case, what if the list has 0 members.
We can get an average return of 0, by forcing total = 0 and member
= 1 for this specific case.
"""

raw_input(prompt)

combo_list = [[k,v] for k,v in combos.iteritems()]
combo_list.sort(key=lambda x: x[0])

prompt="""
We want to now print out a list of all categories by
their averages.  The problem is, dictionaries do 
not gurantee a sort order.  

THe best way to resolve this is
to implicitly convert the dictionary into a list
and then sort it by the keys.  

Why the keys?  It means that states will be seen
side by side, which makes comparisons easier...
"""

raw_input(prompt)


for row in combo_list:
	print(row)

prompt="""
Let's see all the categories by
averages...
"""

raw_input(prompt)

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

prompt="""
Now, I can just look up the state or diagnois or combination that I want.
"""

raw_input(prompt)
