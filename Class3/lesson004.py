print("Pizza Guy: Welcome to Pizza store:")
print("What's a Pizza?")

dough=raw_input("What is pizza dough made of?")
sauce=input("Does pizza have sauce? (True/False)")
cheese=input("Does pizza have cheese? (True/False)")

dough=str(dough)

is_pizza = (dough == 'bread' and sauce == True and cheese == True)
print("Is it really a pizza?")
print(is_pizza)

print("Do you want toppings?  Here is our list:")
Pepperoni = input("Do you want Pepperoni? (True/False)")
Peppers = input("Do you want Peppers? (True/False)")

has_toppings = is_pizza and (Peppers or Pepperoni)
print("you ordered toppings?")
print(has_toppings)

dominos_vendor = raw_input("Where are you ordering pizza (eg dominos)?")
is_dominos = is_pizza and (dominos_vendor != 'dominos')
print("I will cancel if dominos!")
print(is_dominos)