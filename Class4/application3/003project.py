
print("""
	In exercise 2, we replaced ' the ' with " Chris' ".
	The problem is it did not take into consideration
	Capital "The" vs "the" vs "THE".  If you want to 
	do a complete substition, then you need to 
	cast it to something like lower case.  

	We will use kafka_content.find(' the ') to confirm
	that ' the ' is not found.  It should return a 
	-1.
	""")

kafka_file = open('kafka.data','r')

print('reading the file!')
print('Notice that I added lower to the end of read().')
print('everything is lower case now....')
kafka_content = kafka_file.read().lower() 
kafka_content = kafka_content.replace(' the '," Chris' ")

raw_input("Press any key to see text!")
print(kafka_content)

print
raw_input("We can confirm this with str.find('the') command.")
print(kafka_content.find(" the "))
print("-1 means not found!")