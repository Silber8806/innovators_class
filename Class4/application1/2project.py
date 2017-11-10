print("""
	Welcome to Chris' chat parlor...
	we answer questions, soemtimes at a price....
	""")

print("""Part 2 (Answering a Question!): 
	Let's ask a question.
	If the answer is not exit or quit.
	We will just say your name is.
	This is repetitive though!
	""")

while(True):
	user_input = raw_input("What is your name?")

	exit_cmd = (user_input == 'quit' or user_input == 'exit')

	if(exit_cmd):
		print("Exit!")
		break

	print("your name is: %s" % user_input)

