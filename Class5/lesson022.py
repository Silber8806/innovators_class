print("This is a complex list comprehension")

states = ["MA","RI","NH","NM"]
state_dict = {"MA": "Massachusetts",
			  "RI":"Rhode Island", 
			  "NH":"New Hampshire", 
			  "NM": "New Mexico"}

state_names = [state_dict[s] for s in states]
state_abbreviations = zip(state_names,states)

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