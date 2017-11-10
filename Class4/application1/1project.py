print("""
	Welcome to Chris' chat parlor...
	we answer questions, soemtimes at a price....
	""")

print("""Part 1 (Basic Prompt): 
	First problem, we construct a basic prompt system.
	It will start a while loop.  We then except user_input each time.
	If exit or quit is typed in, we exit out of the loop!
	""")

while(True):
	user_input = raw_input(">>>")

	exit_cmd = (user_input == 'quit' or user_input == 'exit')

	if(exit_cmd):
		print("Exit!")
		break

