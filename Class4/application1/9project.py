print("""
	Welcome to Chris' chat parlor...
	we answer questions, soemtimes at a price....
	""")

print("""Part 9:
	I think the q_number parameter is not very 
	intuitive.  Let's convert it to a string.
	We can than match on that string, q_name and
	choose the question that way.  We can break 
	out of the loop using "break" command.
	""")

default_prompt = ">>>"

print("Doctor: how can I help you!")
q_name = "fever"

while(True):
	
	out_phrase="Doctor: interesting..."
	# Question 1!
	if (q_name == "fever"):
		in_phrase = "Do you have a fever (yes/no)?"
		y_q="cough"
		n_q="sick"
	elif (q_name == "sick"):
		in_phrase = "Are you sure, you look sick! (yes/no)?"
		y_q='exit'
		n_q="medicine"
	elif (q_name == "cough"):
		in_phrase = "Do you have a cough (yes/no)?"
		y_q="medicine"
		n_q="sick"
	elif (q_name == "medicine"):
		in_phrase = "Do you want medicine (yes/no)?"
		y_q="dose"
		n_q="sick"
	elif (q_name == "dose"):
		in_phrase = "I can give you an extra dose(yes/no)?"
		y_q="$500"
		n_q="sick"
	elif (q_name == "$500"):
		in_phrase = "Great that will be $500?"
		y_q='exit'
		n_q="sick"
	else:
		in_phrase = ">>>"
		out_phrase = "%s"

	user_input = raw_input(in_phrase)
	print(out_phrase)

	exit_cmd = (user_input == 'quit' or user_input == 'exit')

	if(user_input == "yes"):
		q_name = y_q
	elif(user_input == "no"):
		q_name = n_q

	if (exit_cmd):
		print("Exit!")
		break 
	elif (y_q == 'exit' and user_input == "yes"):
		print("Doctor: Thanks for the visit!")
		break
	elif (n_q == 'exit' and user_input == "no"):
		print("Doctor: Thanks for the visit!")
		break
	elif(q_name == "exit"):
		break




