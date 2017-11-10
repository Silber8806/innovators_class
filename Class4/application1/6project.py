print("""
	Welcome to Chris' chat parlor...
	we answer questions, soemtimes at a price....
	""")

print("""Part 6: 
	Alright, enough with straight forward answers.
	Let's do some more interesting things.
	Let's ask a question in a repetitive fashion.
	We create a program that takes a parameter:
	max_qs, which asks how often we ask a question.
	""")

q_number = 1
default_prompt = ">>>"

while(True):
	curr_q = 0
	max_qs = 1
	if (q_number == 1):
		in_phrase = "What is your name?"
		out_phrase = "Your name is: %s"
	elif (q_number == 2):
		in_phrase = "what is your last name?"
		out_phrase = "Your name is: %s"
	elif (q_number == 3):
		in_phrase = "name five colleagues?"
		out_phrase = "Your colleague is named: %s"
		max_qs = 5
	else:
		in_phrase = ">>>"
		out_phrase = "%s"

	while (curr_q < max_qs):
		user_input = raw_input(in_phrase)

		exit_cmd = (user_input == 'quit' or user_input == 'exit')
		
		if(exit_cmd):
			break

		print(out_phrase % user_input)
		curr_q += 1

	if (exit_cmd):
		print("Exit!")
		break 

	q_number += 1
