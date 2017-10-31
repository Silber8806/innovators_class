speed = 0
speedometer = 'Current speed: %s mph'

if (speed <= 65):
	while(speed < 65):
		speed += 1
		print(speedometer % speed)
else:
	while(speed > 65):
		speed -= 1
		print(speedometer % speed)

print("your are now driving 65 mph!")