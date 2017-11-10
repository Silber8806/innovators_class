# example 1

print("example 1")
i = 0
while(True):
	print(i)
	if (i == 5):
		break
	else:
		i = i + 1

# example 2

print("example 2")
i = 0
while(i <= 10):
	if (i == 5):
		i = i + 1
		continue
	print(i)
	i = i + 1

# example 3

print("example 3")
i = 0
while(i <= 10):
	if (i == 5):
		pass # come to this later
	elif (i == 10):
		pass # fill in at a better time!
	print(i)
	i = i + 1

print("all done!")