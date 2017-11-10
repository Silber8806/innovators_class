print("""
	Welcome to Chris' chat parlor...
	we answer questions, soemtimes at a price....
	""")

print("""Part 4 (): 
	We add more questions to our prompt. 
	We use q_number to guide us through what question to look at.
	We can keep adding more numbers, but that would be pretty boring.
	""")

q_number = 1
default_prompt = ">>>"

while(True):
	if (q_number == 1):
		user_input = raw_input("What is your name?")
	elif(q_number == 2):
		user_input = raw_input("What is your last name?")
	else:
		user_input = raw_input(default_prompt)

	exit_cmd = (user_input == 'quit' or user_input == 'exit')

	if(exit_cmd):
		print("Exit!")
		break
	elif (q_number == 1):
		print("Your first name is: %s" % user_input)
	elif (q_number == 2):
		print("Your last name is: %s" % user_input)

	q_number += 1
