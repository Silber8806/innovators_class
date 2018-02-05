prompt="""
Let's keep our objectives listed here:

1. Knows the balances of all 3 entity types: patient, doctor and insurance company and can report on it.
2. Knows the cost of procedures.
3. Knows if a patient is covered by an insurance policy based on the doctor they visit.
4. Charges the insurance company for a covered portion of the medical procedure.
5. After deducting the insurance portion from the insurance company, charge the patient the final amount.
6. Pay the physician the difference between the two rates.

We will call each of these bullet points a story, develop the feature and then test with our users 
to see if it meets there needs.

We do this in interative fashion.  Develop a feature within a week or so.  Create tests to gurantee
it works as we think.  Then we have users test it (user testing) and see if they agree it meets their
needs.  If not, we makes notes about it and change the above list to figure out the new features.

This procedure is similar (but less detailed) then agile development.
"""

raw_input(prompt)

prompt="""

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



