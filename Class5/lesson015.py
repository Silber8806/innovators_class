customers = {"Johny Walker": True}

todays_customers = ["Johny Walker", "Sarah Walker"]

print("Insert non-existent keys only!")
for customer in todays_customers:
	if (customers.has_key(customer)):
		pass
	else:
		customers[customer] = True
print(customers)


customers = {"Johny Walker": True}

print
print("provide a default value for non-existent keys")
for customer in todays_customers:
	if (customers.get(customer,"N/A") == "N/A"):
		print(customer)

region = {}
region["USA"] = {"States":[]}
region["EU"] = {"Countries":[]}
region["USA"]["States"].extend(["MA","RI"])
region["EU"]["Countries"].extend(["Germany","France","England"])

print
print("A more complex example:")
print(region)

print
print("iterate over USA States:")
for state in region["USA"]["States"]:
	print(state)

print
print("iterate over EU countries")
for country in region["EU"]["Countries"]:
	print(country)

print
print("iterate over states + countries")
for subregion in region["USA"]["States"] + region["EU"]["Countries"]:
	print(subregion)
