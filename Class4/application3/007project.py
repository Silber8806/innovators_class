from collections import Counter

print("""
	We can read a file.  So it makes sense that we 
	should be able to write to a file too.
	Note, writing a file is descructive, it will
	always overwrite it's contents.  Be careful
	when doing this operation.  There is no
	concept of an undo button!
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

kafka_counter = Counter(kafka_words)
print
raw_input("We can feed kafka words into a Counter object.")
print(kafka_counter)

print
raw_input("The Counter object specifically accepts a method Counter.most_common(<number>)!")
print("The 10 most common words are?")
print(kafka_counter.most_common(10))

print
raw_input("Let's write the top 100 words to a file for later use:")
summary = open("kafka_summary.txt",'w')

summary.write('Kafka Analysis:\n')
summary.write(str(kafka_counter.most_common(100)))
