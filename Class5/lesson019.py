print("This is a list comprehension")

states = ["MA","RI","NH","NM"]
state_dict = {"MA": "Massachusetts",
			  "RI":"Rhode Island", 
			  "NH":"New Hampshire", 
			  "NM": "New Mexico"}

print
state_names = [state_dict[s] for s in states]
print("Use the state dict to create a named list of states")
print(state_names)

print
print("This is a short cut for:")
original_states = []
for s in states:
	original_states.append(state_dict[s])
print(original_states)

print
print("You can filter a list (and dict) comprehension using if statement:")
states_with_n = [state_dict[s] for s in states if s.startswith('N')]
print(states_with_n)

print
print("This is a shortcut for:")
n_states = []
for s in states:
	if s.startswith("N"):
		n_states.append(state_dict[s])
print(n_states)

