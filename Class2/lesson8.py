# fruits
apples = 1.99
apple_lb = 2

oranges = 4.99
orange_lb = 1

tax = .075

total = (apples * apple_lb + oranges * orange_lb)
total_tax = total * tax

print("You bought:")
print("apples %s lb: %s" % (apples,apple_lb))
print("oranges %s lb: %s" % (oranges,orange_lb))
print
print("total: %s" % total)
print("total_tax: %s" % total_tax)