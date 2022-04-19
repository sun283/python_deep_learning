import pandas as pd
import matplotlib.pyplot as plt
import math
import numpy as np
import tensorflow as tf

# Tortoise and Hare
# 상수 설정
Tortoise_Speed = 1
Tortoise_Bias = 4
Hare_Speed = 2
MAXVAL = 10
INTERVAL = (MAXVAL*10) + 1
doMeet = False
t_xdata, t_ydata, h_xdata, h_ydata = [],[],[],[]

# Configure figure size
plt.figure(figsize=(10,10))

for t in np.linspace(0, MAXVAL, INTERVAL):
    t_y = Tortoise_Speed*t + Tortoise_Bias
    h_y = Hare_Speed*t
    t_xdata.append(t)
    t_ydata.append(t_y)
    h_xdata.append(t)
    h_ydata.append(h_y)
    if(h_y >= t_y and (not doMeet)):
        doMeet = True
        meetTime = t
        meetDistance = t_y

plt.plot(t_xdata, t_ydata, label='Tortoise')
plt.plot(h_xdata, h_ydata, label='Hare')

if (doMeet):
    plt.title('The hare overcame from '+str(math.ceil(meetTime*100)/100)+'hour(s), '+str(math.ceil(meetDistance*100)/100)+'km(s)', fontsize=16)
    plt.plot(meetTime, meetDistance, 'ro')
else:
    plt.title('They will not meet', fontsize=16)

plt.xlabel('Time(hour)', fontsize=14)
plt.ylabel('Distance(km)', fontsize=14)
plt.legend()
#Show plot
plt.show()

# Tensorflow
learning_rate = 0.01
learning_epochs = 500
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Dense(1, input_dim=1))

# Gradient Descent : Optimizer 최적화
# Stochastic gradient descent(SGD) Optimizer
sgd = tf.keras.optimizers.SGD(learning_rate=learning_rate)
# Squated Error
# Mean Squared Error (MSE) loss function
mse = tf.keras.losses.mean_squared_error

model.compile(loss=mse, optimizer=sgd)

# print summary of the model to the terminal
model.summary()

#Model Training
# The tortoise learning
t_history = model.fit(t_xdata, t_ydata, epochs=learning_epochs)
plt.plot(t_history.history['loss'])
plt.show()
# The Hare learning
h_history = model.fit(h_xdata, h_ydata, epochs=learning_epochs)
plt.plot(h_history.history['loss'])
plt.show()
# Tortoise and Hare
plt.plot(t_history.history['loss'], color='r', label='Tortoise')
plt.plot(h_history.history['loss'], label='Hare')
plt.legend()
plt.show()

# Prediction
result = model.predict([10])
print(result)
p_ydata = model.predict(t_xdata)

# Configure figure size
plt.figure(figsize=(10,10))
plt.plot(h_xdata, h_ydata, 'r*')
plt.plot(h_xdata, p_ydata, color='b')
plt.show()