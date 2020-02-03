from keras.datasets import mnist
from keras import utils, models
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Dropout, Flatten, Dense, Activation
from keras.optimizers import adam

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train = x_train[..., None]
x_test  = x_test[..., None]
x_train = x_train/255 #Normalized
x_test  = x_test/255 #Normalized
print(y_test)
print(x_test.shape)
y_train = utils.to_categorical(y_train, 10)
y_test  = utils.to_categorical(y_test, 10)
print(y_test)

#model creation
model = Sequential()

model.add(Conv2D(32, kernel_size = (3, 3), strides = (1,1), input_shape = (28, 28, 1), activation = "relu"))
model.add(MaxPooling2D((2, 2)))
model.add(Dropout(0.3))
model.add(Conv2D(32, kernel_size = (3, 3), strides = (2,2), input_shape = (28, 28, 1), activation = "relu"))
model.add(Flatten())
model.add(Dropout(0.3))
model.add(Dense(128,activation = "relu"))
model.add(Dropout(0.3))
model.add(Dense(10, activation = 'softmax')) # softmax per il report, output as probability

print(model.summary())

#compile as Classification problem
model.compile(optimizer = adam(lr = 0.002), loss = 'categorical_crossentropy',  metrics = ['accuracy'])
#fit
model.fit(x_train, y_train, batch_size = 64, epochs = 1, validation_split = 0.2)
#save
models.save_model(model, "topmodel")

# To add callbacks
# To add k fold
# To add load.weights
