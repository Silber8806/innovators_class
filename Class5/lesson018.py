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

print
print("we can pair up state abbre with state names using zip:")
state_abbreviations = zip(state_names,states)
print(state_abbreviations)

print
print("This is a short cut for:")
original_zip = []
for indice in range(0,len(states)):
	original_zip.append((state_names[indice],states[indice]))
print(original_zip)

print
print("We can finally convert to dictionary using a comprehension")
state_abbreviations_dict = { k:v for k,v in state_abbreviations}
print(state_abbreviations_dict)

print
print("This is a short-cut for:")
original_dict = {}
for k,v in state_abbreviations:
	original_dict[k] = v
print(original_dict)

print
print("We can do a filter on dictionary comprehensions as well:")
n_shire_state_abbreviations_dict = { k:v for k,v in state_abbreviations if k.endswith("shire") and v.startswith("N")}
print(n_shire_state_abbreviations_dict)

print
print("This is a short-cut for:")
n_shires = {}
for k,v in state_abbreviations:
	if (k.endswith('shire') and v.startswith("N")):
		n_shires[k] = v
print(n_shires)

print
print(
"""
This case paris up all abbrevations with states.  It filters by 
States that start with the same first letter abbreviation as first
letter in their name.
""")
possible_states = [[abbrev,state] for abbrev in state_names for state in states if abbrev[0] == state[0]]
print(possible_states)

print
print("this is short for:")
wow = []
for abbrev in state_names:
	for state in states:
		if (state[0] == abbrev[0]):
			wow.append([abbrev,state])
print(wow)



