prompt="""
Let's keep our objectives listed here:

We add a new feature:
1. Knows the balances of all 3 entity types: patient, doctor and insurance company and can report on it.
2. Knows the cost of procedures.
3. Knows what insurance a patient has.
4. Knows which providers accept certain certain insurance companies.
5. Charges the insurance company for a covered portion of the medical procedure.
6. After deducting the insurance portion from the insurance company, charge the patient the final amount.
7. Pay the physician the difference between the two rates.

We keep building on the above.  The issue from the previous construction is we don't know what rates the 
insurance company pays for a procedure or general coverage.  We need to add a bullet point for that.
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

def get_all_balances(patients,insurances,providers):
	return [get_balance(obj[0],obj[1]) for obj in [patients,insurances,providers]]

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

def calculate_payments(patient,insurance,provider,procedure):
	pay_structure = []
	insurance_payout=0
	procedure_cost=procedures[procedure]["cost"]
	procedure_type=procedures[procedure]["type"]
	if (accepts_insurance(patient,provider)):
		insurance_percent = insurance_coverage(insurance,procedure_type)
		insurance_payout = insurance_percent * procedure_cost
		final_cost = procedure_cost - insurance_payout
	else:
		print("patient insurance is not covered...")
		final_cost = procedure_cost	

	pay_structure.extend([final_cost,insurance_payout])
	return pay_structure

def print_all_balances(patient,insurance,provider):
	patient_balance,insurance_balance,provider_balance = get_all_balances([patients,patient],[insurance_companies,insurance],[providers,provider])
	print("***********************************")
	print("%s:%s" % (patient,patient_balance))
	print("%s:%s" % (provider,provider_balance))
	print("%s:%s" % (insurance,insurance_balance))
	print("***********************************")
	return 0

def calculate_final_balances(patient,insurance,provider,procedure,insurance_pay, patient_pay):
	balances = []
	patient_balance,insurance_balance,provider_balance = get_all_balances([patients,patient],[insurance_companies,insurance],[providers,provider])
	procedure_cost=procedures[procedure]["cost"]
	final_insurance_balance = insurance_balance - insurance_pay
	final_balance = patient_balance - patient_pay
	final_provider_balance= provider_balance + procedure_cost
	balances.extend([final_balance,final_insurance_balance,final_provider_balance])

	if (final_balance < 0 or final_insurance_balance < 0):
		print("someone can't afford this operation!")
		return 1

	set_balance(patients,patient,final_balance)
	set_balance(insurance_companies,insurance,final_insurance_balance)
	set_balance(providers,provider,final_provider_balance)

	print("***********************************")
	print("total cost: %s" % procedure_cost)
	print("insurance paid: %s" % insurance_pay)
	print("patient due: %s" % patient_pay)
	print("***********************************")

	return 0

def process_transactions(stringify_json):
	transactions = json.loads(stringify_json)
	for mid,tran in transactions.iteritems():
		medical_id = mid
		patient = tran['patient']
		procedure = tran['procedure']
		provider = tran['provider']

		print("***********************************")
		print("***********************************")
		print("TRANSACTION %s:" % medical_id)
		print("***********************************")
		print("***********************************")
		medical_procedure(patient,procedure,provider)
		print
		print
		print
	return 0

def create_test_json():
	import random 

	tran_dict = {}
	for i in range(1,10):
		tran = []
		patient = random.choice(patients.keys())
		procedure = random.choice(procedures.keys())
		provider = random.choice(providers.keys())
		tran = {"patient":patient,"procedure": procedure,"provider": provider}
		tran_dict[i] = tran

	stringify_json = json.dumps(tran_dict,indent=4)
	print("transactions:")
	print(stringify_json)

	raw_input("processing above JSON!")

	return stringify_json

def medical_procedure(patient,procedure,provider):
	""" 
	This is a procedure to calculate medical procedure impact on 
	patient, doctor and insurance company based on some procedure.
	"""

	insurance=patients[patient]['insurance']

	print("patient: %s" % patient)
	print("insurance: %s" % insurance)
	print("procedure: %s" % procedure)
	print("provider: %s" % provider)

	if (not valid_transaction(patient,procedure)):
		return 1

	print_all_balances(patient,insurance,provider)

	final_cost, insurance_payout = calculate_payments(patient,insurance,provider,procedure)

	calculate_final_balances(patient,insurance,provider,procedure,insurance_payout,final_cost)

	print_all_balances(patient,insurance,provider)

	return 0


def main():
	""" main entry point of program """ 
	medical_json = create_test_json()
	process_transactions(medical_json)
	return 0

if __name__ == "__main__":
	main()



