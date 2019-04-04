import numpy as np
from encoder import get_encoded_data

def get_converted_data_to_spikes():
	ts_data = get_encoded_data()
	
	spike_times = []

	spike_rate_sensory_cortex = 0.00029
	
	for i in range(len(ts_data)):
		cur_spike_times = [list() for k in range(len(ts_data[0][0]-1))]
		for sec in range(len(ts_data[0])):
			for f in range(1, len(ts_data[0][0])):
				interval = ts_data[i][sec][f]

				isi = np.random.poisson(spike_rate_sensory_cortex*(1-interval), 1000)
				x = np.arange(1000)
				x = x[isi>0]
				x += sec*1000
				cur_spike_times[f-1]+=x.tolist()
		
		spike_times.append(cur_spike_times)
	return spike_times
