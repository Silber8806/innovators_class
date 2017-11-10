print("""
	Welcome to Chris' chat parlor...
	we answer questions, soemtimes at a price....
	""")

print("""Part 8:
	We can do a more complicated example.
	Let's take a doctors visit!  We can
	answer many questions and come to 
	two separate conclusions.  
	Either you want medicine in which
	the doctor asks for an extra dose
	at $500.  You can say you are
	sure you are not sick!
	You can see complex logic in action!
	""")

q_number = 1
default_prompt = ">>>"

print("Doctor: how can I help you!")

while(True):
	
	out_phrase="Doctor: interesting..."
	# Question 1!
	if (q_number == 1):
		in_phrase = "Do you have a fever (yes/no)?"
		y_q=10
		n_q=2
	elif (q_number == 2):
		in_phrase = "Are you sure, you look sick! (yes/no)?"
		y_q='exit'
		n_q=11
	elif (q_number == 10):
		in_phrase = "Do you have a cough (yes/no)?"
		y_q=11
		n_q=2
	elif (q_number == 11):
		in_phrase = "Do you want medicine (yes/no)?"
		y_q=100
		n_q=2
	elif (q_number == 100):
		in_phrase = "I can give you an extra dose(yes/no)?"
		y_q=101
		n_q=2
	elif (q_number == 101):
		in_phrase = "Great that will be $500?"
		y_q='exit'
		n_q=2
	else:
		in_phrase = ">>>"
		out_phrase = "%s"

	user_input = raw_input(in_phrase)
	print(out_phrase)

	exit_cmd = (user_input == 'quit' or user_input == 'exit')

	if (exit_cmd):
		print("Exit!")
		break 

	if(y_q != 'exit'):
		y_q -= 1

	if(n_q != 'exit'):
		n_q -= 1

	if (y_q == 'exit' and user_input == "yes"):
		print("Doctor: Thanks for the visit!")
		break
	if (n_q == 'exit' and user_input == "no"):
		print("Doctor: Thanks for the visit!")
		break

	if(user_input == 'yes'):
		q_number=y_q
	elif(user_input == 'no'):
		q_number=n_q
	else:
		q_number -= 1

	q_number += 1