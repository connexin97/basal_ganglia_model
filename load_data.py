import numpy as np

def get_data_from_file(file_name):
	with open("data/"+file_name,"r") as f:
		current_data = f.read().split()
	current_data = np.array(current_data , "float64")
	current_data = np.reshape(current_data , (len(current_data)//13 , 13))
	return current_data

def load_data():
	types = ["als", "control", "park", "hunt"]
	numbers = [13, 16, 15, 20]
	ts_data = list()
	type_data = list()

	for i in range(len(types)):
		for j in range(1 ,numbers[i]+1):
			current_type = types[i]
			ts_data.append(get_data_from_file(current_type+str(j)+".ts"))
			type_data.append(current_type)
	return np.array(ts_data)  ,np.array(type_data)

ts_data  , type_data = load_data()
