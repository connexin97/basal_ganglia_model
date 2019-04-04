from ANNarchy import *
import my_neuron
#############################################################
def get_neuron_type():
	return Izhikevich#my_neuron.IF

def get_layers_names():
	layers = ['Sensory_Cortex', 'Motor_Cortex', 'SNC', 'STN',
						 'GPe', 'GPi/SNr', 'Striatum', 'Thalamus' ]
	return layers

def get_layers_number_of_neurons():
	
	layers = get_layers_names()
	number_of_neurons = [10 for i in range(len(layers))]
	number_of_neurons[0] = 13
	layers_number_of_neurons = dict(zip(layers ,  number_of_neurons))
	return layers_number_of_neurons

def make_single_connection(pre , post , type):
	layers = get_layers_names()
	return [layers.index(pre), layers.index(post), type]

def get_connections():

	Graph = [ 
				('Sensory_Cortex', 'SNC', 'exc'),
				('Sensory_Cortex', 'Striatum', 'exc'),
				('Motor_Cortex', 'STN', 'exc'),
				('Motor_Cortex', 'Striatum', 'exc'),
				('SNC', 'Striatum', 'exc'),
				('STN', 'GPi/SNr' , 'exc'),
				('STN', 'SNC', 'exc'),
				('STN', 'GPe', 'exc'),
				('GPe', 'STN', 'inh'),
				('GPe', 'GPi/SNr', 'inh'),
				('GPi/SNr', 'Thalamus', 'inh'),
				('Striatum', 'GPi/SNr', 'inh'),
				('Striatum', 'GPe', 'inh'),
				('Thalamus', 'Motor_Cortex', 'exc'),
				
				]
	connections = []
	for e in Graph:
		connections.append(make_single_connection(e[0],e[1],e[2]))

	return connections

def get_weight_range(type):
	if(type == 'exc'):
		return Uniform(10 , 15)
	return -Uniform(10 , 15)

