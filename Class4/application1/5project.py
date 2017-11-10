print("""
	Welcome to Chris' chat parlor...
	we answer questions, soemtimes at a price....
	""")

print("""Part 5: 
	Let's make it easier to read.
	The previous section made it hard to understand.
	The question and answer were in separate parts of
	The code.  Let's have them all under one if statement.
	""")

q_number = 1
default_prompt = ">>>"

while(True):
	if (q_number == 1):
		in_phrase = "What is your name?"
		out_phrase = "Your name is: %s"
	elif (q_number == 2):
		in_phrase = "what is your last name?"
		out_phrase = "Your name is: %s"
	else:
		in_phrase = ">>>"
		out_phrase = "%s"

	user_input = raw_input(in_phrase)

	exit_cmd = (user_input == 'quit' or user_input == 'exit')
	if(exit_cmd):
		print("Exit!")
		break

	print(out_phrase % user_input)

	q_number += 1
