import numpy as np
from encoder import get_encoded_data
from ANNarchy import *

def get_converted_data_to_spikes():
	ts_data = get_encoded_data()
	spike_times = [[[1000/max(ts_data[k][j][i] , 1e-6)+ j*1000
					for i in range(len(ts_data[0][0]))]
						for j in range(len(ts_data[0])) ]
							for k in range(len(ts_data))]
	return spike_times

def compile_model():
	spike_times = get_converted_data_to_spikes()
	inputs = SpikeSourceArray(spike_times=spike_times[0])
	m = Monitor(inputs, 'spike')
	compile()
	return m

m = compile_model()
simulate(10000.)

data = m.get('spike')
t, n = m.raster_plot(data)

import matplotlib.pyplot as plt
plt.plot(t, n, '.')
plt.ylim(0, 100)
plt.xlabel('Time (ms)')
plt.ylabel('# neuron')
plt.show()
