prompt="""
The first step of building any software is to 
talk to the people that will use it and 
understanding the "requirements".

Requirements are like they sound, a set 
of requirements or needs that the software 
should fufill to be considered complete.

The set of tasks that an Application (software program)
are called it's feature set.  A feature is a task or 
ability of the software.

Press Enter to get a sense of the requirements discovery process.
"""

raw_input(prompt)

prompt="""
We are hired by a hospital to re-design the medical billings 
portion of their software.  They had a previous software 
that was handling this function, but it currently isn't powerful
enough to deal with future requests.  They decided to hire 
you to produce a basic software application, which can be 
easily extended in the future.

The first thing we do is a set of interviews.  The interviews give
us a sense of the type of things that a typical user will do and 
how the software can solve it.

One of the things the doctor and patient care coordinator tells you
about is the inability to track balances between 3 entities.  The 
doctor, the patient and the insurance company.  They want you to 
create a system that will mediate the payments between these 3 
entities.

They tell you that they need software that:
1. Knows the balances of all 3 entity types: patient, doctor and insurance company and can report on it.
2. Knows the cost of procedures.
3. Knows if a patient is covered by an insurance policy based on the doctor they visit.
4. Charges the insurance company for a covered portion of the medical procedure.
5. After deducting the insurance portion from the insurance company, charge the patient the final amount.
6. Pay the physician the difference between the two rates.

We will add more complexity aftewards, but this seems like a good set of tasks to begin with.

We begin our software application construction, by defining the 3 entites available:
1. Patient
2. Provider
3. Insurance Company

We can then start by defining a function to handle a medical transaction.
"""

raw_input(prompt)

procedures = {"blood shot": 200}
patients = {"Sam":2000,"Jane":500,"Marty":250000}
providers = {"Mass General":500000,"Mt Auburn": 350000,"St. Mary":50000}
insurance_companies= {"Aetna":1000000,"Tufts":500000,"Harvard Pilgrim":25000}

def medical_procedure(patient,procedure):
	""" 
	This is a procedure to calculate medical procedure impact on 
	patient, doctor and insurance company based on some procedure.
	"""
	if (patients.has_key(patient) and procedures.has_key(procedure)):
		final_balance = patients[patient] - procedures[procedure]
		if (final_balance > 0):
			print("%s balance is: %s" % (patient, final_balance))
			patients[patient] = final_balance
		else:
			print("Patient balance is insufficient")
			return 1
	else:
		print("patient or procedure does not exist!")
		return 1
	return 0


def main():
	""" main entry point of program """ 
	medical_procedure("Jane","blood shot")
	return 0

if __name__ == "__main__":
	main()



