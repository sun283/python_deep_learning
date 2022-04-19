# This code is working on google colab
# needs to be altered using pydrive
# Mount Drive
# from google.colab import drive
# drive.mount('/gdrive')
import matplotlib.pyplot as plt
import pandas as pd
import tensorflow as tf
import numpy as np

file = '/gdrive/My Drive/data/data_2021.csv'
data = pd.read_csv(file)
plt.rc('font', family='NanumBarunGothic')

#101 서울, 105 기흥, 110 목천, 115 대전, 120 황간, 125 남구미, 130 동김천, 135 경주, 140 부산
#101 서울(406.94), 105 기흥(387.19), 110 목천(329.91), 115 대전(271.94), 120 황간(222.38), 125 남구미(167.25), 130 동김천(192.00), 135 경주(68.26), 140 부산(0)
#Distance from Seoul : 0, 19.75, 77.03, 135, 184.56, 214.94, 239.69, 338.68, 406.94
# Distance from Seoul : 0, 20, 77, 135, 185, 240, 215, 339, 407
data['도착영업소코드'] = data['도착영업소코드'].map({105: 20, 110: 77, 115: 135, 120: 185, 125: 240, 130: 215, 135: 339, 140: 407})
data.rename(columns={'도착영업소코드': '거리'}, inplace=True)

# Linear Regression by Tensorflow
Selected_Date = '2021-01-10' #@param {type:"date"}
input_date = int(Selected_Date.replace('-',''))
print(input_date)

data_date = data[data['집계일자'] == input_date]
data_time = data_date.groupby(['집계일자','거리'])['통행시간'].mean()
data_out = data_time.reset_index()

plt.plot(data_date['거리'], data_date['통행시간'], 'r*')

# Dataframe to List
data_list = data_out.values.tolist()
data_list[:3]

x_train = [int(r[1]) for r in data_list]
y_train = [int(r[2]/10) for r in data_list]

plt.plot(x_train, y_train, 'r*')

# -8승
learning_rate = 1e-8
learning_epochs = 2000
# Stochastic gradient descent (SGD) Optimizer
sgd = tf.keras.optimizers.SGD(learning_rate=learning_rate)
# Mean Square Error (MSE) loss function
mse = tf.keras.losses.mean_squared_error
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Dense(1, input_dim=1))
model.compile(loss=mse, optimizer=sgd)
print(model.summary())

#Train the model
history = model.fit(x_train, y_train, epochs=learning_epochs)

plt.plot(history.history['loss'])
plt.show()

Distance = 500 #@param {type:"slider", min:0, max:500, step:1}
input_data = [Distance]
predicted_value = model.predict(input_data)
print('%3d km takes %5.1f seconds on %s' %(Distance, predicted_value[0][0]*10, Selected_Date))