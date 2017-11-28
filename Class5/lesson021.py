print("This is a dictionary comprehension")

states = ["MA","RI","NH","NM"]
state_dict = {"MA": "Massachusetts",
			  "RI":"Rhode Island", 
			  "NH":"New Hampshire", 
			  "NM": "New Mexico"}

state_names = [state_dict[s] for s in states]
state_abbreviations = zip(state_names,states)

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

