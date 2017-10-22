legs = 2
arms = 2
limbs = arms + legs

print("I am a:")
if (limbs == 0):
	print("snake!")
elif(limbs > 4):
	print("centipede")
elif(legs == 2):
	print("Ostrich")
elif(legs == 2 and arms == 2):
	print("Human")
else:
	print("I have no clue?")


