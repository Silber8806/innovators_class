prompt="""
The first step of building any software is to 
talk to the people that will use it and 
understanding the "requirements".

Requirements are like they sound, a set 
of requirements or needs that the software 
should fufill to be considered complete.

The set of tasks that an Application solves (software program)
are called it's feature set.  A single task that a software
solves is called a feature.

Press Enter to get a sense of the requirements discovery process.
"""

raw_input(prompt)

prompt="""
You are a distinguished developer at a startup.  You’ve developed many applications.  
An entrepreneurial doctor approaches you.  The doctor owns a health-related practice 
and has many thousand patients a day each with different procedures.  He can’t hire enough 
experts in medical billing.  He also knows that many other hospitals and practices are facing 
this dilemma.  He wants to hire you to prototype a medical billing system.  If it works, 
he’ll give you 25-40% cut of the subscription business he plans to build on top of 
your software (he’s got 2-3 other co-founders).  You begin your journey!
We can then start by defining a function to handle a medical transaction.
"""

raw_input(prompt)

prompt="""
You: Good morning, Dr. Pal.  How can I assist you?
Pal: My staff are having a lot of issues processing medical records, specifically billing!  
You: What are the steps for handling medical billing?
Pal: We conduct a procedure.  We have an internal spreadsheet containing all the costs for different procedures.  We then look up the patient's insurance and see how much is covered!  We then separate the bill into 2 different segments.  The first one goes to the insurance company, which pays the amount first.  We then take the difference between the procedure cost and the insurance payout.  We call this the patient due.  We bill the patient.  Hopefully, both the insurance company and the patient then pay their bills.  Otherwise, it might go to collections.
You: hmmm… let me think about this problem!
"""

raw_input(prompt)

prompt="""
The doctor in this scenario is called the product owner.  He also comes up with “requirements”.  Requirements are as they sound, 
the required tasks a program should accomplish.  We can think of each task as a “feature”.  All tasks or abilities a 
software has is called its feature set.  What are the medical billing requirements:

1. We can look up procedures and costs.
2. We can look up patient by name and find out their insurance provider.
3. We can look up insurance providers to see if they are accepted by the hospital.
4. If a patient has coverage, we should be able to look up what percent of the cost is covered.
5. We should be able to bill the insurance provider.  
6. We should calculate the bill after the insurance pays out it’s portion.  We should then bill the patient the remainder.
7. If a patient insurance is not accepted by the provider, we should bill the patient the patient the entire procedure cost.
8. If the patient or the insurance company run out of funds, we should cancel the transaction and talk to them directly.
9. If the bill was paid by both the insurance company and/or the patient.  The provider should receive payment equivalent to the procedure cost.

"""

raw_input(prompt)

prompt="""
In software development, it is worth breaking down 
complex problems into simpler ones. 

We begin first by creating the 4 entities involved in the requirements: 

     provider
     patient
     insurance company 
     procedure

we can do this by creating a dictionary for each type.  The dictionary 
contains the name of the entity (key) followed by a dollar figure.
Either the entities balance or for procedures: the procedure cost.
"""

raw_input(prompt)

prompt="""
After defining some basic entities, we create a function that encapsulates
the logic behind the medical transaction.  We then begin to create logic
in that function and build out functionality.  We do this incrementally,
by first focusing on a simple problem and then expanding the logic from 
there.

In this case, we focus on only one entity, the patient, and him paying the
entire cost of the medical bill.

The logic we check for:
1. Does the patient and procedure exist.
2. Can the patient pay the procedure cost.
3. If the patient can, deduct the amount from the patients balance.
"""

raw_input(prompt)

prompt="""
Did you notice the section with:

    medical_procedure("Jane","blood shot")

When we right software, we will often do small tests
or executions.  This is done so that we can see
the behavior of the program and judge if it is 
correct.

When functions test True/False assertions, we call
them tests.  Several tests will often check the behavior
of a specific function, these tests are called unit
tests.

When a function tests behavior between two software 
systems and checks for behavior, it is called a 
integration test!
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



