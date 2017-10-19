# Simple Denoising auto encoder
import numpy as np
from keras.layers import Input, Dense
from keras.models import Model

# creating toy data
e_dim = 32 # encoding dimension
seq_len = 64 # length of sequence
high = 10 # high
low = 0 # low
examples = 100 # training examples

# Creating data
data_x = np.random.randint(high = high, low = low, size = (examples, seq_len))

# Creating noisy data
noise_factor = 0.3
data_noisy = data_x + noise_factor*np.random.random(size = data_x.shape)

# defining input
input_seq = Input(shape = (seq_len,))

# defining dense layers
encoded = Dense(e_dim)(input_seq)
decoded = Dense(seq_len, activation = 'relu')(encoded)

# defining auto-encoder
autoencoder = Model(input_seq, decoded)

# defining encoder and decoder seperately, so they can be called later
encoder = Model(input_seq, encoded)

# defining placeholder for decoder module
encoded_input = Input(shape=(e_dim,))
# retrieve the last layer of the autoencoder model
decoder_layer = autoencoder.layers[-1]
# create the decoder model
decoder = Model(encoded_input, decoder_layer(encoded_input))

# compiling the model
autoencoder.compile(optimizer = 'Adam', loss = 'mean_squared_error')

# training the model
autoencoder.fit(data_noisy, data_x, epochs = 1000, verbose = 0)

# getting outputs of encoders or decoder
print(data_x[0])
ei = encoder.predict(data_x)
di = decoder.predict(ei)
print(di[0])
ai = autoencoder.predict(data_x)
print(ai[0])
