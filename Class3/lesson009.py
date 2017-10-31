print("What trail will we choose?")
print("Our criteria:")
elevation = raw_input("elevation(ft):")
length = raw_input("length(mi):")
fitness = input("are you fit? (True/False)")
is_rain = input("Is it raining (True/False)")

elevation = int(elevation)
length = int(length)

is_easy = (elevation <= 200 and length <5) or length <= 1
is_medium = (elevation >= 200 and elevation <= 500) and length >= 1

if (fitness == False):
	trail_type = 'easy'
elif(is_easy):
	trail_type = 'easy'
elif (is_medium and is_rain):
	trail_type = 'easy'
elif (is_medium):
	trail_type = 'medium'
else:
	trail_type = 'hard'

print("you should take:")
print(trail_type + ' trail')