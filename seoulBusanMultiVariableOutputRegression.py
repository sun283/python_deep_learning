# This code is working on google colab
# needs to be altered using pydrive
# Mount Drive
# from google.colab import drive
# drive.mount('/gdrive')
import matplotlib.pyplot as plt
import pandas as pd
import tensorflow as tf
import numpy as np
from mpl_toolkits import mplot3d

plt.rc('font', family='NanumBarunGothic')
file = '/gdrive/My Drive/data/data_2021_1_12.csv'
data = pd.read_csv(file)

#101 서울, 105 기흥, 110 목천, 115 대전, 120 황간, 125 남구미, 130 동김천, 135 경주, 140 부산
#101 서울(406.94), 105 기흥(387.19), 110 목천(329.91), 115 대전(271.94), 120 황간(222.38), 125 남구미(167.25), 130 동김천(192.00), 135 경주(68.26), 140 부산(0)
#Distance from Seoul : 0, 19.75, 77.03, 135, 184.56, 214.94, 239.69, 338.68, 406.94
# Distance from Seoul : 0, 20, 77, 135, 185, 240, 215, 339, 407
data['도착영업소코드'] = data['도착영업소코드'].map({105: 20, 110: 77, 115: 135, 120: 185, 125: 240, 130: 215, 135: 339, 140: 407})
data.rename(columns={'도착영업소코드': '거리'}, inplace=True)
data_destination = data[data['거리'].isin([135, 407])]
data_time = data_destination.groupby(['집계시','요일','거리'])['통행시간'].mean()
data_distance = data_time.unstack(level=-1)
data_distance.dropna()
data_out = data_distance.reset_index()
data_list = data_out.values.tolist()
#Train Dataset
x_train = [ r[:2] for r in data_list ]
y_train = [ [r[-1]] for r in data_list ]

# Multi Variable and Output using Tensorflow
learning_rate = 1e-4
learning_epochs = 5000

#Stochastic gradient descent (SGD) Optimizer
sgd =  tf.keras.optimizers.SGD(learning_rate=learning_rate)
# Mean Square Error (MSE) loss function
mse = tf.keras.losses.mean_squared_error
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Dense(2, input_shape=(2,)))
model.compile(loss=mse, optimizer=sgd)
print(model.summary())

# Train the model
history = model.fit(x_train, y_train, epochs=learning_epochs)

plt.figure(figsize=(10,10))
plt.plot(history.history['loss'])
plt.title('Cost Gradient Decent')
plt.ylabel('Total Cost')
plt.xlabel('Number of Training')
plt.show()

print("%20s %20s " % ('Step', 'Cost')+'\n')
for step in range(learning_epochs):
    if step % 100 == 0:
        cost_val = history.history['loss'][step]
        print("%20i %20.5f" %(step, cost_val))
        
# Prediction
Time = 14
Day = 3
time_condition = data_out['집계시'] == Time
day_condition = data_out['요일'] == Day
selected_data = data_out[time_condition & day_condition]

input = [ Time, Day ]
time = model.predict([input])
distance = [ 135, 407 ]

plt.figure(figsize=(10,10))
p_xdata, p_ydata = [], [] 
r_ydata = [selected_data[135], selected_data[407]]

print("%20s %20s %20s %20s" % ('거리(km)', '실제', '예측', '차이')+'\n')
for index in range(len(time[0])):
    dist_time = time[0][index]
    real_time = r_ydata[index]
    variation = real_time - dist_time
    p_xdata.append(distance[index])
    p_ydata.append(dist_time)
    print("%20d %20f %20f %20i" % (distance[index], real_time, dist_time, variation)+'\n')

plt.plot(p_xdata, r_ydata, 'r*', label='Read record')
plt.plot(p_xdata, p_ydata, 'bo', label='Predicted record')
plt.title('Predicted Records')
plt.ylabel("Time(seconds)")
plt.xlabel("Distance(km)")
plt.legend()
plt.show()