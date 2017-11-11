
print("""
	Python can ask the operating system to open and read a file.
	We do this with the open command.  
	open(<file_name>,<r|w|a>)
	The first parameter is a relative or absolute reference to a file.
	The second parameter tells the computer if you want to read, write over or append to the 
	end of a file.
	""")

kafka_file = open('kafka.data','r')

print("This line does a complete read of the file.")
print("It will read it into a string!")
kafka_content = kafka_file.read()

raw_input("Press any key to see text!")
print(kafka_content)