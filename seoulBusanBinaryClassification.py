# This code is working on google colab
# needs to be altered using pydrive
# Mount Drive
# from google.colab import drive
# drive.mount('/gdrive')
import matplotlib.pyplot as plt
import pandas as pd
import tensorflow as tf
import numpy as np

plt.rc('font', family='NanumBarunGothic')
file = '/gdrive/My Drive/data/data_2021_1_12.csv'
data = pd.read_csv(file)

#101 서울, 105 기흥, 110 목천, 115 대전, 120 황간, 125 남구미, 130 동김천, 135 경주, 140 부산
#101 서울(406.94), 105 기흥(387.19), 110 목천(329.91), 115 대전(271.94), 120 황간(222.38), 125 남구미(167.25), 130 동김천(192.00), 135 경주(68.26), 140 부산(0)
#Distance from Seoul : 0, 19.75, 77.03, 135, 184.56, 214.94, 239.69, 338.68, 406.94
# Distance from Seoul : 0, 20, 77, 135, 185, 240, 215, 339, 407
data['도착영업소코드'] = data['도착영업소코드'].map({105: 20, 110: 77, 115: 135, 120: 185, 125: 240, 130: 215, 135: 339, 140: 407})
data.rename(columns={'도착영업소코드': '거리'}, inplace=True)
data_destination = data[data['거리']==407]
data_time = data_destination.groupby(['집계시','요일','거리'])['통행시간'].mean()
data_distance = data_time.unstack(level=-1)
data_distance.dropna()
data_out = data_distance.reset_index()
stat = data_out.describe()
mean_value = stat[407][1]
data_out['Binary'] = data_out[407] > mean_value
data_out['Binary'] = data_out['Binary'].map({True: 1, False: 0})

# Dataframe to List
data_list = data_out.values.tolist()
# Train dataset
x_train = [ r[:2] for r in data_list ]
y_train = [ [r[-1]] for r in data_list ]

learning_rate = 1e-4
learning_epochs = 5000
# Stochastic gradient descent (SGD) Optimizer
sgd = tf.keras.optimizers.SGD(learning_rate=learning_rate)
# Mean Square Error (MSE) loss function
mse = tf.keras.losses.mean_squared_error
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Dense(1, input_shape=(2,), activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer=sgd, metrics=['accuracy'])
print(model.summary())

# Train the model
history = model.fit(x_train, y_train, epochs=learning_epochs)

plt.figure(figsize=(10,10))
plt.plot(history.history['loss'], color='r', label='비용')
plt.plot(history.history['accuracy'], color='b', label='정확도')
plt.title('비용과 정확도')
plt.ylabel('비용, 정확도')
plt.xlabel('학습량')
plt.legend()
plt.show()

print("%20s %20s %20s" % ('학습량', '비용', '정확도')+'\n')
for step in range(learning_epochs):
    if step % 100 == 0:
        cost_val = history.history['loss'][step]
        acc_val = history.history['accuracy'][step]
        print("%20i %20.5f %20.5f" % (step, cost_val, acc_val))
        
# Prediction
Time = 14
Day = 3

time_condition = data_out['집계시'] == Time
day_condition = data_out['요일'] == Day
selected_data = data_out[time_condition & day_condition]

input = [Time, Day]
result = model.predict([input])
print("%10s %20s" % ('결과값', '지연여부')+'\n')
if(result[0] > 0.5):
    print("%10.7f %20s" % (result[0], '지연'))
else:
    print("%10.7f %20s" % (result[0], '시간 내 도착'))