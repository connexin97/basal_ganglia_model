import numpy as np
from keras.layers import Input, LSTM, RepeatVector
from keras.models import Model
from load_data import load_data
from keras.callbacks import EarlyStopping


def fix_size_of_data(ts_data):
	reconstructed_ts_data = np.zeros((len(ts_data) , 120 , 13))
	for i in range(len(ts_data)):
		reconstructed_ts_data[i] = ts_data[i][:120 , :]
	return reconstructed_ts_data

def normalize(ts_data):
	for i in range(len(ts_data[0][0])):
		mini  = ts_data[:,:,i].min()
		maxi = ts_data[:,:,i].max()
		ts_data[:,:,i] = (ts_data[:,:,i]-mini)/(maxi-mini)
	return ts_data

def get_encoder(ts_data):
	timesteps = len(ts_data[0])
	input_dim = len(ts_data[0][0])
	latent_dim = 15
	inputs = Input(shape=(timesteps, input_dim))
	encoded = LSTM(latent_dim , dropout=0.75)(inputs)

	decoded = RepeatVector(timesteps)(encoded)
	decoded = LSTM(input_dim, return_sequences=True)(decoded)

	sequence_autoencoder = Model(inputs, decoded)
	sequence_autoencoder.compile(optimizer='adam', loss='mse')
	sequence_autoencoder.fit(ts_data, ts_data, epochs=1000,
							batch_size=len(ts_data), shuffle=True ,
							validation_split = 1/10, callbacks = [EarlyStopping(monitor='val_loss',patience = 5)] )
	encoder = Model(inputs, encoded)
	return encoder

def get_encoded_data():
	ts_data , type_data = load_data()
	ts_data = fix_size_of_data(ts_data)
	ts_data = normalize(ts_data)
	encoder = get_encoder(ts_data)
	return encoder.predict(ts_data)

get_encoded_data()