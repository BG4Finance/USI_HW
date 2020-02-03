import joblib
import numpy as np


def load_data(filename):
    """
    Loads the data from a saved .npz file.
    ### YOU CAN NOT EDIT THIS FUNCTION ###
    :param filename: string, path to the .npz file storing the data.
    :return: two numpy arrays:
        - x, a Numpy array of shape (n_samples, n_features) with the inputs;
        - y, a Numpy array of shape (n_samples, ) with the targets.
    """
    data = np.load(filename)
    x = data['x']
    y = data['y']

    return x, y


def evaluate_predictions(y_true, y_pred):
    """
    Evaluates the mean squared error between the values in y_true and the values
    in y_pred.
    ### YOU CAN NOT EDIT THIS FUNCTION ###
    :param y_true: Numpy array, the true target values from the test set;
    :param y_pred: Numpy array, the values predicted by your model.
    :return: float, the the mean squared error between the two arrays.
    """
    return ((y_true - y_pred) ** 2).mean()


def load_model(filename):
    """
    Loads a Scikit-learn model saved with joblib.dump.
    This is just an example, you can write your own function to load the model.
    Some examples can be found in src/utils.py.
    :param filename: string, path to the file storing the model.
    :return: the model.
    """
    model = joblib.load(filename)

    return model

import numpy as np
x,y = load_data("data.npz")
print(x.shape)
print(y.shape)

# Perform linear regression
XX = np.linalg.inv(x.T @ x)
EsT= XX @ x.T @ y
print(EsT)

from keras.datasets import mnist
from keras import utils, models
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Dropout, Flatten, Dense, Activation
from keras.optimizers import adam
from keras.callbacks import EarlyStopping
from sklearn.model_selection import train_test_split

STOP = EarlyStopping(monitor='val_loss', mode='min', patience=50)
y    = np.reshape(y, (-1,1))
x, x_test, y, y_test = train_test_split(x, y, test_size=0.15)

#model creation
model = Sequential()

model.add(Dense(2000,activation="relu"))
model.add(Dense(500,activation="relu"))
model.add(Dense(100,activation="relu"))
model.add(Dense(10,activation="relu"))
model.add(Dense(1, activation='elu'))

#compile as Classification problem
model.compile(optimizer=adam(lr=0.0005), loss='mse')
#fit
storia = model.fit(x, y, batch_size=64, epochs=2000, validation_split=0.2,callbacks=[STOP])
#save
models.save_model(model, "nlmodel")


#Val_loss valdation
print(np.asarray(storia.history["val_loss"]).min())

#Val_loss test
estimation = model.predict(x_test)
evaluate_predictions(y_test, estimation)
