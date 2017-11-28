like_a_string = ['H','E','L','L','O','_','W','O','R','L','D','!']

print "Example 1:"
for letter in like_a_string:
	print(letter)

print
print "Example 2:"
print(like_a_string[0])
print(like_a_string[-1])
print(like_a_string[5:])

mixed_container = [1,2,3,'Hello World','H','E','L','L','O',1.5]

print
print "Example 3:"
for element in mixed_container:
	print(element)