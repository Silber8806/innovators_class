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



