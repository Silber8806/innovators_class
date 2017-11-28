a_list_of_lists = [[0,1],[0,2],[0,"Hello World!"],[0,["another list"]]]

print("Example 1:")
for lst in a_list_of_lists:
	print(lst)

print
print("Example 2:")
for lst in a_list_of_lists:
	for l in lst:
		print(l)

print
print("Example 3:")
print(a_list_of_lists[0][0])