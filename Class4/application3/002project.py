
print("""
	Some common words in the english language include.
	The and the.  Let's replace all occurrences of
	' the ' with ' Chris' ' just to have a bit of fun.
	""")

kafka_file = open('kafka.data','r')

print('reading the file!')
kafka_content = kafka_file.read()
kafka_content = kafka_content.replace(' the '," Chris' ")

raw_input("Press any key to see text!")
print(kafka_content)