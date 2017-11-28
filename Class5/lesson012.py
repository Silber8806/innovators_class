print("What is a tuple:")
customer_info = ("John","Smith","United States",25)

print("Tuples are like lists, but you can't modify them:")
print("indexing:")
print(customer_info[0])
print(customer_info[0:1])

print
print("for loop:")
for tup in customer_info:
	print("info: %s" % tup)

print("It fails on any command below:")
customer_info[0] = "Judy"
customer_info.insert(1,1)
customer_info.remove("United States")
print(customer_info.pop())
customer_info.sort()
customer_info.reverse()

