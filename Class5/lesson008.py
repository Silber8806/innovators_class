print("This is our list:")
best_list = [4,5,6]
print(best_list)

print
print("Change a member by index:")
best_list[0] = 100
print(best_list)

print
print("Assign best_list to another list")
silly_list = best_list
print(silly_list,best_list)

print
print("Let's change best_list again...")
best_list[0] = 1000
print(silly_list,best_list)

print
print("What Happened?????")

print
print("best_list is actually silly_list")
print(best_list == silly_list)

