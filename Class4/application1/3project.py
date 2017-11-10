print("""
	Welcome to Chris' chat parlor...
	we answer questions, soemtimes at a price....
	""")

print("""Part 3 (Clearing the prompt): 
	How do we force the chat program to stop asking for my name.
	The answer is, we change the input based on an if statement.
	We then append a segment that manages the input in this situation.
	""")

q_number = 1

while(True):
	if (q_number == 1):
		user_input = raw_input("What is your name?")
	else:
		user_input = raw_input(">>>")

	exit_cmd = (user_input == 'quit' or user_input == 'exit')

	if(exit_cmd):
		print("Exit!")
		break
	elif (q_number == 1):
		print("Your name is: %s" % user_input)
		q_number += 1