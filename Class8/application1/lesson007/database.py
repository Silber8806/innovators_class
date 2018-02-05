import json

providers = """
	{
		"Mass General": {
			"accepts": [
				"Aetna",
				"Tufts",
				"Harvard Pilgrim"
			],
			"balance":500000
		},
		"Mt Auburn": {
			"accepts": [
				"Aetna",
				"Tufts"
			],
			"balance":350000
		},
		"St. Mary": {
			"accepts": [
				"Aetna",
				"Tufts",
				"Harvard Pilgrim"
			],
			"balance":50000
		}	
	}
"""

patients = """
	{
		"Sam":{
			"balance":2000,
			"insurance":"Aetna"
		},
		"Jane":{
			"balance":500,
			"insurance":"Tufts"
		},
		"Marty":{
			"balance":250000,
			"insurance":"Harvard Pilgrim"
		}
	}
"""

procedures = """
	{
		"blood shot":{
			"cost": 200,
			"type": "lab"
		},
		"check-up":{
			"cost": 50,
			"type": "preventative"
		}
	}
"""

insurance_companies = """
	{
		"Aetna":{
			"balance":1000000,
			"policies":{
				"preventative":100,
				"lab":80
			}
		},
		"Tufts":{
			"balance":500000,
			"policies":{
				"preventative":100,
				"lab":80
			}
		},
		"Harvard Pilgrim":{
			"balance":25000,
			"policies":{
				"preventative":100,
				"lab":80
			}
		}
	}
"""

def get_balance(collection,entity):
	return collection[entity]['balance']

def set_balance(collection,entity, value):
	if (value >= 0):
		collection[entity]['balance'] = value
		return 0
	else:
		return 1

providers = json.loads(providers)
patients = json.loads(patients)
procedures = json.loads(procedures)
insurance_companies = json.loads(insurance_companies)


