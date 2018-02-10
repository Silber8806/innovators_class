prompt="""
The medical_procedure function was getting very long.  When
a function gets really long it is often hard to follow.

I decided to take some of the logic out of medical_procedure
and create new functions to cover that code.  The new functions
are:

	calculate_payments : calculates the insurance and patient portions
	of the payment.  Returns a pay_structure list that contains both
	charges.

	print_all_balances : we are constantly printing the balance
	either before or after a transaction.  Figuring out the state
	of all entities involved in a transaction is a great debugging 
	too.  We isolate this print functionality here.

	calculate_final_balances : this is the function that goes through
	all entities and updates their remaining balances.  

Once we are done, the medical_procedure function is significantly smaller
and easier ot read.  Function calls also reflect their specific purpose.
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
	patient_balance,insurance_balance,provider_balance = get_all_balances([patients,patient],\
																		  [insurance_companies,insurance],\
																		  [providers,provider])
	print
	print("CURRENT BALANCE:")
	print("%s:%s" % (patient,patient_balance))
	print("%s:%s" % (provider,provider_balance))
	print("%s:%s" % (insurance,insurance_balance))
	print("CURRENT BALANCE:")
	print
	return 0

def calculate_final_balances(patient,insurance,provider,procedure,insurance_pay, patient_pay):
	balances = []
	patient_balance,insurance_balance,provider_balance = get_all_balances([patients,patient],\
																		  [insurance_companies,insurance],\
																		  [providers,provider])
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

	print
	print("TRANSACTION:")
	print("total cost: %s" % procedure_cost)
	print("insurance paid: %s" % insurance_pay)
	print("patient due: %s" % patient_pay)
	print("TRANSACTION:")
	print

	return 0


def medical_procedure(patient,procedure,provider):
	""" 
	This is a procedure to calculate medical procedure impact on 
	patient, doctor and insurance company based on some procedure.
	"""

	insurance=patients[patient]['insurance']

	if (not valid_transaction(patient,procedure)):
		return 1

	print_all_balances(patient,insurance,provider)

	final_cost, insurance_payout = calculate_payments(patient,insurance,provider,procedure)

	calculate_final_balances(patient,insurance,provider,procedure,insurance_payout,final_cost)

	print_all_balances(patient,insurance,provider)

	return 0


def main():
	""" main entry point of program """ 
	medical_procedure("Jane","blood shot","Mass General")
	return 0

if __name__ == "__main__":
	main()



