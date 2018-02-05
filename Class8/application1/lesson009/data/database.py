import json

data_dir = './data/'
file_names = ['insurance.json', 'patient.json','procedure.json','provider.json']
data_files = [data_dir + file for file in file_names]

def load_json_data(json_file):
	with open(json_file,'r') as f:
		return json.loads(f.read())

def load_all_files(files):
	data_files = []
	for f in files:
		json_data = load_json_data(f)
		data_files.extend([json_data])
	return data_files

def get_balance(collection,entity):
	return collection[entity]['balance']

def set_balance(collection,entity, value):
	if (value >= 0):
		collection[entity]['balance'] = value
		return 0
	else:
		return 1