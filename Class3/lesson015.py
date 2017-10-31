print("exercise 1")
i = 1
while(i <= 1000000):
	print(i)
	i = i + 1

print("exercise 2")
i = 1
while(i <= 1000000):
	if(i % 2 == 0):
		print(i)
	i = i + 1

print("exercise 3")
sequence = 10
times_to_print = 100
i = 1

while(i <= times_to_print):
	print("%s times!" % i)
	j = 1
	while(j <= sequence):
		print(j)
		j = j + 1
	i = i + 1