wheels = 2
enclosed = True

if (wheels == 2):
	if (enclosed == False):
		print("Motorcycle!")
	else:
		print("Lit motor bike!")
elif (wheels == 4):
	if (enclosed == True):
		print("Coup car!")
	else:
		print("Convertible car!")
# optional else stateemnt
else:
	print("Not a car or motorcycle!")