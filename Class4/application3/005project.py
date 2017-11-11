from collections import Counter

print("""
	Let's say we want to go through all the words in a 
	text and count it that way.  It would be way more
	accurate.  How would we do that?

	We could use the split command, which separates the 
	text into words based on spaces.  We can then
	give the word list to a object called a Counter.

	To do so, add:

	from collections import Counter

	to make the Counter available in your code.

	Counter is a special python object that makes counting easy!
	""")

kafka_file = open('kafka.data','r')
kafka_content = kafka_file.read().lower().replace('\n','')

print
raw_input("After using: kafka_content.read().lower().strip('\n'), press any key!")
print(kafka_content)

kafka_words = kafka_content.split(' ')

print
raw_input("After using the kafka_content.split(' '), press any key!")
print(kafka_words)

print
raw_input("We can feed kafka words into a Counter object.")
print(Counter(kafka_words))

print
raw_input("The Counter object specifically accepts a method Counter.most_common(<number>)!")
print("The 10 most common words are?")
print(Counter(kafka_words).most_common(10))