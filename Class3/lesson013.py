vehicle_id = 1
max_number_of_cars = 50
make='ford'
model='mustang'
wheels = 4
seats = 2

report=""
report+="Number %s:\n"
report+="Make: %s; Model: %s\n" % (make, model)
report+="Wheels: %s; Seats:%s\n" % (wheels, seats)

while(vehicle_id <= max_number_of_cars):
	print(report % vehicle_id)
	vehicle_id += 1

print("factory cool down!")