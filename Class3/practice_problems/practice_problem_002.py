# Count the number of even and odd numbers from the series of numbers:
# numbers=(155,77,3,2,55,75,3,94,49)

numbers = (155, 77 ,3 ,2 ,55, 75, 3, 94, 49)
count_odd = 0
count_even = 0
i = -1
number_count=len(numbers)
while (i+1 < number_count):
	i=i+1
	if (numbers[i] % 2 == 0):
		count_even+=1
	else:
		count_odd+=1
print("Number of even numbers:", count_even)
print("Number of odd numbers:",count_odd)