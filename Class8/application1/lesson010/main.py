import json
import click
import tests.test as test
from data.database import *

@click.group()
def cli():
    """
    A command line client used for doing medical records processing.
    Use this API to look up records etc....
    """
    pass

insurance_companies, patients, procedures, providers =  load_all_files(data_files)

prompt="""

"""

raw_input(prompt)

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

@cli.command(help="-do the medical prodecure: requires <patient> <procedure> <provide>!")
@click.argument('patient',nargs=1)
@click.argument('procedure',nargs=1)
@click.argument('provider',nargs=1)
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

@cli.command(help="-run the tests for this module!")
def run_tests():
	""" main entry point of program """ 
	medical_json = test.create_test_json(patients,procedures,providers)
	process_transactions(medical_json)
	return 0

if __name__ == '__main__':
    cli()

