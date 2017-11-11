from collections import Counter

print("""
	Let's combine alice in wonder land, frankenstein and kafka text.
	Then do the analysis again!
	""")

kafka_file = open('kafka.data','r')
kafka_content = kafka_file.read().lower().replace('\n','')

alice_file = open('kafka.data','r')
alice_content = kafka_file.read().lower().replace('\n','')

frank_file = open('kafka.data','r')
frank_content = kafka_file.read().lower().replace('\n','')

all_content = kafka_content +  alice_content + frank_content

print
raw_input("Combine the 3 texts, press any key!")
print(all_content)

all_words = all_content.split(' ')

print
raw_input("After using the all_content.split(' ') to get words, press any key!")
print(all_words)

print
raw_input("We can feed kafka words into a Counter object.")
print(Counter(all_words))

print
raw_input("The Counter object specifically accepts a method Counter.most_common(<number>)!")
print("The 10 most common words are?")
print(Counter(all_words).most_common(10))