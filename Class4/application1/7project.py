print("""
	Welcome to Chris' chat parlor...
	we answer questions, soemtimes at a price....
	""")

print("""Part 7: 
		We can also create workflows by choosing
		a new number for q_number.  q_number = 0
		would be the first question and q_number 2
		would be the second number.
	""")

q_number = 0
default_prompt = ">>>"

while(True):
	curr_q = 0
	max_qs = 1

	q_number += 1
	
	if (q_number == 1):
		in_phrase = "Who is your boss?"
		out_phrase = "Your name is: %s"
		q_number = 1
	elif (q_number == 2):
		in_phrase = "Who reports to him?"
		out_phrase = "Your name is: %s"
		q_number = 0
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
