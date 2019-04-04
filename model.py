import numpy as np
from ANNarchy import *
import matplotlib.pyplot as plt
from sklearn.preprocessing import scale
from my_synapse import my_STDP
import parameters
from data_to_spikes import get_converted_data_to_spikes
#spike pattern parameters

#########################################################
""" TODO
	weight_ranges
	data_to_spike : signs
	train with all data

"""

def make_connection(prepop , postpop , type_of_synapse , weight_range):
	proj = Projection(prepop , postpop ,target = type_of_synapse,  synapse = my_STDP)
	proj.connect_all_to_all(weights = weight_range )
	return

#weights + number of neurons
def make_populations(layers_number_of_neurons , inputs):

	population_of_layers = []
	for layer in layers_number_of_neurons.keys():
		population_of_layers.append(Population(layers_number_of_neurons[layer] , parameters.get_neuron_type()))
	population_of_layers [0] = inputs

	return population_of_layers

def make_all_connections(population_of_layers):

	connections = parameters.get_connections()

	for connection in connections:
		prepop = population_of_layers[connection[0]]
		postpop = population_of_layers[connection[1]]
		type_of_synapse = connection[2]
##############################################################
		weight_range = Uniform(0, 17)
		make_connection( prepop, postpop, type_of_synapse, weight_range)


	#gpi has poisson
	input_of_thalamus = PoissonPopulation(name = 'input_of_thalamus', geometry=10, rates=0.1)
	proj = Projection(pre = input_of_thalamus,
					  post = population_of_layers[-1],
					  target = 'exc', synapse = my_STDP)

	proj.connect_all_to_all(weights=Uniform(0, 17))


	return 0


def compile_model():

	spike_times = get_converted_data_to_spikes()
	inputs = SpikeSourceArray(spike_times=spike_times[0])

	population_of_layers = make_populations(parameters.get_layers_number_of_neurons(), inputs)
	make_all_connections(population_of_layers)

	outputs = []
	for i in range(len(population_of_layers)):
		outputs.append(Monitor(population_of_layers[i],'spike'))
	compile()
	return outputs

#plot all layers
def plot_monitor(outputs):
	# print(len(outputs))
	name_of_layers = parameters.get_layers_names()
	plt.figure(figsize=(10,10))
	for i in range(2):
		for j in range(4):
			m = outputs[i*4+j]
			data = m.get('spike')
			t, n = m.raster_plot(data)
			n+=1
			plt.subplot(2, 4, i*4+j+1 )
			plt.plot(t, n, '.')
			plt.ylim(0, 13)
			#plt.xlim(0, 120000)
			#plt.xlabel('Time (ms)')
			#plt.ylabel('# neuron')
			plt.title(name_of_layers[i*4+j])
	plt.show()

outputs = compile_model()
simulate(120000.)
plot_monitor(outputs)
