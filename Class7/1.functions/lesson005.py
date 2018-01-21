prompt="""
Let"s see the power of functions by writing a quick
application to process medical claims.

I recently had a small injury on my finger.  The 
insurance company processes a claim.  The data they provide:

Member Rate, Amount plan will pay and Amount due!

Note, I"m not a medical record specialist, so I might
be making some of this up!
"""

raw_input(prompt)

def main():
	return 0

prompt="""
Let"s start with a main function.
It"s common practice to have a single
entry point to your code called main!
"""

raw_input(prompt)

patients = {"Sam":2000,"Jane":500,"Marty":250000}
providers = {"Mass General":500000,"Mt Auburn": 350000,"St. Mary":50000}
insurance_companies= {"Aetna":1000000,"Tufts":500000,"Harvard Pilgrim":25000}

def main():
	return 0

prompt="""
Let"s create some entities and then think about it 
from a systems perspective.

There is the provider, patients and an insurance 
company.  Let"s say we want to keep track of the
balances between the 3 entities: patients, providers and 
insurance companies.

We could host a dictionary to do this!
"""

raw_input(prompt)


patients = {"Sam":2000,"Jane":500,"Marty":250000}
providers = {"Mass General":500000,"Mt Auburn": 350000,"St. Mary":50000}
insurance_companies= {"Aetna":1000000,"Tufts":500000,"Harvard Pilgrim":25000}

def procedure(patient):
	cost = 500
	patients[patient] -= cost
 	return 0

def main():
	print(patients["Sam"])
	procedure("Sam")
	print(patients["Sam"])
	return 0

main()

prompt="""
We know that the cost of a procedure will have a lot of
calculations.  One way we can handle this is by creating
a function, which we can than call.  Any changes in:
procedure is then isolated.

Let"s begin with the case that all costs are passed through
the patient.
"""

raw_input(prompt)

import json


providers = """
	{
		"Mass General": {
			"accepts": [
				"Aetna",
				"Tufts",
				"Harvard Pilgrim"
			],
			"balance":500000
		},
		"Mt Auburn": {
			"accepts": [
				"Aetna",
				"Tufts"
			],
			"balance":350000
		},
		"St. Mary": {
			"accepts": [
				"Aetna",
				"Tufts",
				"Harvard Pilgrim"
			],
			"balance":50000
		}	
	}
"""


providers = json.loads(providers)
patients = {"Sam":2000,"Jane":500,"Marty":250000}
insurance_companies= {"Aetna":1000000,"Tufts":500000,"Harvard Pilgrim":25000}

def procedure(patient,doctor):
	cost = 500
	balance = patients[patient] - cost
	if balance > 0:
		patients[patient] = balance
		providers[doctor]['balance'] += cost
		return 0
	else:
 		return 1

def main():
	print(patients["Sam"])
	procedure("Sam","Mass General")
	print("sam balance:")
	print(patients["Sam"])
	print("doctor balance:")
	print(providers["Mass General"])

	return 0

main()

prompt="""
Let"s extend the code we have so that the doctor or provider
gets  paid at the expense of the patient.  The patient of 
course can"t pay if he has negative balance, so we should 
add that logic in now as well!
"""

raw_input(prompt)

import json

providers = """
	{
		"Mass General": {
			"accepts": [
				"Aetna",
				"Tufts",
				"Harvard Pilgrim"
			],
			"balance":500000
		},
		"Mt Auburn": {
			"accepts": [
				"Aetna",
				"Tufts"
			],
			"balance":350000
		},
		"St. Mary": {
			"accepts": [
				"Aetna",
				"Tufts",
				"Harvard Pilgrim"
			],
			"balance":50000
		}	
	}
"""

providers = json.loads(providers)
patients = {"Sam":2000,"Jane":500,"Marty":250000}
insurance_companies= {"Aetna":1000000,"Tufts":500000,"Harvard Pilgrim":25000}

def insurance_member_rate(doctor,insurance):
	accepts = providers[doctor]["accepts"]
	if insurance in accepts:
		discount = 400
	else:
		discount = 0
	return discount

def procedure(patient,doctor,insurance):
	cost = 500
	discount = insurance_member_rate(doctor,insurance)
	patient_cost = cost - discount
	insurance_cost = discount
	balance = patients[patient] - patient_cost
	if balance > 0:
		patients[patient] = balance
		insurance_companies[insurance] -= discount
		providers[doctor]['balance'] += cost
		return 0
	else:
 		return 1

def main():

	patient = "Sam"
	insurance = "Aetna"
	doctor = "Mass General"

	print("before:")
	print("patient balance: %s" % str(patients[patient]))
	print("doctor balance: %s" % str(insurance_companies[insurance]))
	print("insurance balance: %s" % str(providers[doctor]['balance']))

	procedure(patient,doctor, insurance)

	print("after:")
	print("patient balance: %s" % str(patients[patient]))
	print("doctor balance: %s" % str(insurance_companies[insurance]))
	print("insurance balance: %s" % str(providers[doctor]['balance']))

	return 0

main()

prompt="""
Let's extend this to include a member rate, which involves
a discount based on your insurance provider.  The above
procedure costs 500, but the insurance company will cover
400 if the provider is accepts it.
"""

raw_input(prompt)


import json

providers = """
	{
		"Mass General": {
			"accepts": [
				"Aetna",
				"Tufts",
				"Harvard Pilgrim"
			],
			"balance":500000
		},
		"Mt Auburn": {
			"accepts": [
				"Aetna",
				"Tufts"
			],
			"balance":350000
		},
		"St. Mary": {
			"accepts": [
				"Aetna",
				"Tufts",
				"Harvard Pilgrim"
			],
			"balance":50000
		}	
	}
"""

patients = """
	{
		"Sam":{
			"balance":2000,
			"insurance":"Aetna"
		},
		"Jane":{
			"balance":500,
			"insurance":"Tufts"
		},
		"Marty":{
			"balance":250000,
			"insurance":"Harvard Pilgrim"
		}
	}
"""

providers = json.loads(providers)
patients = json.loads(patients)
insurance_companies= {"Aetna":1000000,"Tufts":500000,"Harvard Pilgrim":25000}

def process_all_claims(claims,doctor):
	for c in claims:
		procedure(c,doctor)

	return 0

def report_balances(patient,doctor):
	insurance = patients[patient]['insurance']
	print("before:")
	print("patient balance: %s" % str(patients[patient]['balance']))
	print("doctor balance: %s" % str(insurance_companies[insurance]))
	print("insurance balance: %s" % str(providers[doctor]['balance']))
	return 0

def insurance_member_rate(doctor,insurance):
	accepts = providers[doctor]["accepts"]
	if insurance in accepts:
		discount = 400
	else:
		discount = 0
	return discount

def procedure(patient,doctor):
	cost = 500
	insurance = patients[patient]['insurance']

	report_balances(patient,doctor)
	discount = insurance_member_rate(doctor,insurance)
	patient_cost = cost - discount
	insurance_cost = discount
	balance = patients[patient]['balance'] - patient_cost
	if balance > 0:
		patients[patient]['balance'] = balance
		insurance_companies[insurance] -= discount
		providers[doctor]['balance'] += cost
		changed_balance=0
	else:
 		changed_balance=1

 	report_balances(patient,doctor)
 	return changed_balance

def main():

	patient = ["Sam","Jane","Marty","Marty"]
	doctor = "Mass General"

	print("batch processing claims...")

	process_all_claims(patient,doctor)

	print("finished processing")

	return 0

main()

prompt="""
Let's add a report_balances function to handle all the printing.
Also, let's make insurance a property of the patient by converting
it to a JSON object.  We also add a process_all_claims function
to process all patients at once.

Exercise for reader:
1. modify the above code to handle more procedures!  Remember:
Each hospital has a different rate for each prodecure.  The 
insurance company might have a different rate for the procedure
for each doctor.  How do you handle the doctor-insurance company
combination!
"""

raw_input(prompt)

prompt="""
Thought exercise:
> Functions let you name repeatable tasks.  This makes the code significantly
more readable.
> Functions can be used to encapsulate code that changes often or is complex.
People can rely on the function accomplishing something without getting into
the deeper details.  They can also be used to create expectations.  EG...

	I want to run a machine learning model.  I don't understand how it works,
	but I just want it to run and give me a list of categories for the data 
	I input.

Next, how functions are actually social.  Not in the dinner party type of way!
"""

raw_input(prompt)


