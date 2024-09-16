import json
import pickle
import numpy as np

__data_columns = None
__model = None
__locations = None

def get_location_name():
	global __locations
	global __data_columns
	with open(r"prediction\model\columns.json", "r") as f:
		__data_columns = json.load(f)['data_columns']
		__locations = __data_columns[3:]
		return __locations
	

def load_model():
	global __model
	with open(r"prediction\model\bangalore_house_price_prediction_model.pkl", "rb") as f:
		__model = pickle.load(f)
		print(__model)


def predict_price(location, sqft, bhk, bath):
	global __model
	global __data_columns
	global __locations
	try:
		loc_index = __data_columns.index(location.lower())
	except:
		loc_index = -1

	x = np.zeros(len(__data_columns))
	x[0] = sqft
	x[1] = bhk
	x[2] = bath
	if loc_index >= 0:
		x[loc_index] = 1

	return round(__model.predict([x])[0], 2)
	

