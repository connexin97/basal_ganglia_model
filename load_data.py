import numpy as np

def load_data():
    types = ["als", "control", "park", "hunt"]
    numbers = [13, 16, 15, 20]
    ts_data = []
    type_data = []

    for i in range(len(types)):
        for j in range(1, numbers[i] + 1):
            current_type = types[i]
            ts_data.append(np.loadtxt("data/" + current_type + str(j) + ".ts"))
            type_data.append(current_type)
    return np.array(ts_data), np.array(type_data)


ts_data, type_data = load_data()
