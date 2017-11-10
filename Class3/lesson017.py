vehicle_id = 1
max_number_of_vehicles = 500

vehicle0 = 'Mustang'
vehicle1 = 'Civic'
vehicle2 = "Ninja (motorcycle"
line_item = 'vehicle: %s is a %s'

while(vehicle_id <= max_number_of_vehicles):
	if(vehicle_id % 3 == 0):
		vehicle_type = vehicle0
	elif(vehicle_id % 3 == 1):
		vehicle_type = vehicle1
	elif(vehicle_id % 3 == 2):
		vehicle_type = vehicle2
	print(line_item % (vehicle_id, vehicle_type))
	vehicle_id += 1

print("factory cool down!")