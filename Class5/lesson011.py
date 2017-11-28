lots_of_numbers = [4,3,2,1,0,9,8,7,6,5]

print("original:")
print(lots_of_numbers)

print("Sorting:")
lots_of_numbers.sort()
print(lots_of_numbers)

print("Reverse Sort:")
lots_of_numbers.reverse()
print(lots_of_numbers)

print("Sort then reverse sort:")
lots_of_numbers.sort()
lots_of_numbers.sort(reverse=True)
print(lots_of_numbers)

print("Another Sort!")
sorted(lots_of_numbers)
print(lots_of_numbers)