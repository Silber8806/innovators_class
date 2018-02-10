prompt="""
After developing the patient relationship to the procedure, we 
decide to tackle the insurance company logic.  We want to 
separate this logic into a few steps.   The first step
is to figure out if an insurance company is accepted by 
a provider.  To create this relationship, we have to:

1. figure out what the patient's insurance is.
2. figure out if the provider accepts the insurance.

To do this, we replace the providers and patient dicts 
with two JSON objects.  The first, providers, now has 
a property accepts for each hospital, which lists 
all the acceptable insurance policies.  It also has
a balance property for it's bank balance.

The patients dict is also turned into a JSON object.  It
has an insurance property and a balance.  The insurance
property is the patients current insurance.
"""

raw_input(prompt)

prompt="""
When developing the logic, I decided to split up some
tasks as helper functions.  I created:

    get_balance - get the bank balance of any entity.
    valid_transaction - check if all the entities mention exist.
    accepts_insurance - check if an insurance company is accepted by a provider.

We can use these functions within medical_procedure, to simplify things 
and make it more readable.
"""

raw_input(prompt)


prompt="""
The medical_procedure function can be split into two parts.  The first
checks if a transaction is valid, if it is, it splits the payment into
insurance and patient portion.  If the insurance is not accepted, it 
just assigns the entire cost to the patient's bill.

The second part of the logic, adjusts the balances of patient.  We
purposely don't tackle the insurance company yet, by making the 
insurance payout = 0 as a placeholder.  

We can tackle the calculation of the insurance payment next.  This 
is worth doing as the doctor has not specified hte logic yet!
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

procedures = {"blood shot": 200}
insurance_companies= {"Aetna":1000000,"Tufts":500000,"Harvard Pilgrim":25000}

def get_balance(collection,entity):
	return collection[entity]['balance']

def valid_transaction(patient,procedure):
	if (patients.has_key(patient) and procedures.has_key(procedure)):
		return 1
	else:
		return 0

def accepts_insurance(patient,provider):
	patient_insurance = patients[patient]['insurance']
	providers_accepted = providers[provider]['accepts']
	if ( patient_insurance in providers_accepted):
		return True
	else:
		return False

def medical_procedure(patient,procedure,provider):
	""" 
	This is a procedure to calculate medical procedure impact on 
	patient, doctor and insurance company based on some procedure.
	"""
	insurance=patients[patient]['insurance']
	procedure_cost=procedures[procedure]

	print("%s insurance is %s." % (patient,insurance))

	if (valid_transaction(patient,procedure)):
		if (accepts_insurance(patient,provider)):
			insurance_payout =0 
			print("%s covers %s cost" % (insurance, insurance_payout))
			final_cost = procedure_cost - insurance_payout
		else:
			print("patient insurance is not covered...")
			final_cost = procedure_cost
	else:
		return 1

	print("%s final payment due is %s" % (patient,final_cost))

	patient_balance = get_balance(patients,patient)
	insurance_balance = insurance_companies[insurance]

	print("balance before transaction...")
	print("%s balance: %s" % (patient, patient_balance))
	print("%s balance: %s" % (insurance, insurance_balance))

	final_balance = patient_balance - final_cost

	print("final balance is: %s" % final_balance)

	if (final_balance > 0):
		patients[patient]['balance'] = final_cost
		print("%s final balance: %s" % (patient,final_balance))
	else:
		print("%s can't afford procedure" %(patient))
		print
		return 1

	print
	return 0


def main():
	""" main entry point of program """ 
	medical_procedure("Jane","blood shot","Mass General")
	return 0

if __name__ == "__main__":
	main()



