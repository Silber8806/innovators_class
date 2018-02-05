import json

def create_test_json(patients, procedures,providers):
	import random 

	tran_dict = {}
	for i in range(1,10):
		tran = []
		patient = random.choice(patients.keys())
		procedure = random.choice(procedures.keys())
		provider = random.choice(providers.keys())
		tran = {"patient":patient,"procedure": procedure,"provider": provider}
		tran_dict[i] = tran

	stringify_json = json.dumps(tran_dict,indent=4)
	print("transactions:")
	print(stringify_json)

	raw_input("processing above JSON!")

	return stringify_json

