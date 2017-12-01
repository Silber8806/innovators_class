# This is a range function

print("this is a range function:")
for number in range(0,10):
	print(number)

print
print("range produces a sequence")
print("It starts with the first number")
print("It goes to n-1 from the second number")
print(range(0,10))

print
print("You can use range to go through indexes")
print("this mimics traditional way for loops are")
print("done in languages like js and C:")
print("len is the count of container members..")
print

pandora_box = ["Turtle","Mountain","Goat","astro"]

for box_mem in range(0,len(pandora_box)):
	print(pandora_box[box_mem])

print("This is the same result as doing a for loop!")
print("The benefit is you can access index nubmers...")