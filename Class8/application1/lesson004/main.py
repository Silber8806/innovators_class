prompt="""
We continue from the previous lesson focusing now exclusively on 
developing the logic for calculating what the insurance company
owes and applying it to the new balance.

We first expand both the procedures and insurance companies into json 
objects with 2 new properties each.  These properties are:

	procedure:
	cost - cost of a procedure
	type - the type of the procedure

	insurance_companies:
	balance - bank balance
	policies - types of procedures covered with percents.

We also create a few new functions:

	insurance_coverage - this is a helper function that retrieves
	the coverage percent based on company and procedure type.
	set_balance - this modifies the JSON file by overwriting
	the balance.

We use these new functions to calculate the insurance_payout 
and set the balance for patient, provider and insurance_company.

see the new logic below:
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

procedures = """
	{
		"blood shot":{
			"cost": 200,
			"type": "lab"
		},
		"check-up":{
			"cost": 50,
			"type": "preventative"
		}
	}
"""

insurance_companies = """
	{
		"Aetna":{
			"balance":1000000,
			"policies":{
				"preventative":100,
				"lab":80
			}
		},
		"Tufts":{
			"balance":500000,
			"policies":{
				"preventative":100,
				"lab":80
			}
		},
		"Harvard Pilgrim":{
			"balance":25000,
			"policies":{
				"preventative":100,
				"lab":80
			}
		}
	}
"""

providers = json.loads(providers)
patients = json.loads(patients)
procedures = json.loads(procedures)
insurance_companies = json.loads(insurance_companies)

def get_balance(collection,entity):
	return collection[entity]['balance']

def set_balance(collection,entity, value):
	if (value >= 0):
		collection[entity]['balance'] = value
		return 0
	else:
		return 1

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

def insurance_coverage(insurance,procedure_type):
	return insurance_companies[insurance]["policies"][procedure_type] / 100.0

def medical_procedure(patient,procedure,provider):
	""" 
	This is a procedure to calculate medical procedure impact on 
	patient, doctor and insurance company based on some procedure.
	"""
	insurance=patients[patient]['insurance']
	procedure_cost=procedures[procedure]["cost"]
	procedure_type=procedures[procedure]["type"]

	print("%s insurance is %s." % (patient,insurance))

	if (valid_transaction(patient,procedure)):
		if (accepts_insurance(patient,provider)):
			insurance_percent = insurance_coverage(insurance,procedure_type)
			insurance_payout = insurance_percent * procedure_cost
			print("%s covers %s cost" % (insurance, insurance_payout))
			final_cost = procedure_cost - insurance_payout
		else:
			print("patient insurance is not covered...")
			final_cost = procedure_cost
	else:
		return 1

	print("%s final payment due is %s" % (patient,final_cost))

	patient_balance = get_balance(patients,patient)
	insurance_balance = get_balance(insurance_companies,insurance)
	provider_balance =  get_balance(providers,provider)

	print("balance before transaction...")
	print("%s balance: %s" % (patient, patient_balance))
	print("%s balance: %s" % (insurance, insurance_balance))

	final_insurance_balance = insurance_balance - insurance_payout
	final_balance = patient_balance - final_cost

	print("final balance is: %s" % final_balance)
	print("final insurance payout is: %s" % final_insurance_balance)

	if (final_balance > 0):
		set_balance(patients,patient,final_cost)
		print("%s final balance: %s" % (patient,final_balance))
	else:
		print("%s can't afford procedure" %(patient))
		print
		return 1

	if (final_insurance_balance > 0):
		set_balance(insurance_companies,insurance,final_insurance_balance)
		print("%s final balance: %s" % (insurance,final_insurance_balance))
	else:
		print("%s can't afford procedure" %(insurance))
		print
		return 1

	final_provider_balance= provider_balance + procedure_cost
	set_balance(providers,provider,final_provider_balance)

	print("balance after transaction...")
	print("%s balance: %s" % (patient, final_balance))
	print("%s balance: %s" % (insurance, final_insurance_balance))
	print("%s balance: %s" % (provider, final_provider_balance))

	print
	return 0


def main():
	""" main entry point of program """ 
	medical_procedure("Jane","blood shot","Mass General")
	return 0

if __name__ == "__main__":
	main()



