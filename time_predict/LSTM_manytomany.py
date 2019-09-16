from keras.utils import plot_model
from keras.layers import LSTM,Dense
from keras.models import Sequential

# define model【Vanilla LSTM】
model = Sequential()
model.add(LSTM(100, activation='relu', return_sequences=True, input_shape=(4, 1)))
model.add(LSTM(100, activation='relu'))
model.add(Dense(2))
model.compile(optimizer='adam', loss='mse')



plot_model(model, to_file='model.png')