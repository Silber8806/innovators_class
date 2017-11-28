that_list = [1,2,3]

print("Inserting:")
that_list.insert(2,100)
print(that_list)

print("Removing:")
that_list.remove(1)
print(that_list)

print("extending:")
that_list.extend([1,2,3])
print(that_list)

print("appending:")
that_list.append([1,2,3])
print(that_list)

print("popping!")
popped = that_list.pop()
print(that_list, popped)

print("Let's count!")
that_list.count()

print("Let's find things:")
print(that_list.find(1))
print(that_list.find("hi!"))