# first refactor

wheels = 2
enclosed = True

if (wheels == 2 and enclosed == False):
	print("motorcycle")
elif(wheels == 2 and enclosed == True):
	print("Lit motor bike!")
elif(wheels == 4 and enclosed == False):
	print("Convertible Car")
elif(wheels == 4 and enclosed == True):
	print("Coup Cart!")
else:
	print("Non-traditional vehicle!")

# second refactor

vehicle_type = 'car'
enclosed = True

if (vehicle_type == 'motorcycle' and enclosed == False):
	print("motorcycle")
elif(vehicle_type == 'motorcycle' and enclosed == True):
	print("Lit motor bike!")
elif(vehicle_type == 'car' and enclosed == False):
	print("Convertible Car")
elif(vehicle_type == 'car' and enclosed == True):
	print("Coup Cart!")
else:
	print("Non-traditional vehicle!")
