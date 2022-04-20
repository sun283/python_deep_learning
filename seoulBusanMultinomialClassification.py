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
data_destination = data[data['거리'].isin([407])]
data_time = data_destination.groupby(['집계시','요일','거리'])['통행시간'].mean()
data_distance = data_time.unstack(level=-1)
data_distance.dropna()
data_out = data_distance.reset_index()
stat = data_out.describe()
value_25 = stat[407][4]
value_75 = stat[407][6]
data_out['Grade'] = 0

def get_grade(input):
    if input > value_25:
        if input > value_75:
            output = 2
        else:
            output = 1
    else:
        output = 0
    return output

data_grade = pd.DataFrame(columns=['time', 'day', 'grade'])

for index, item in data_out.iterrows():
    print(index, item['집계시'], item['요일'])
    data_grade = data_grade.append({
        'time': item['집계시'],
        'day': item['요일'],
        'grade': get_grade(item[407])
    }, ignore_index=True)
    
# Dataframe to List
data_list = data_grade.values.tolist()
# Train dataset
x_train = [ r[:2] for r in data_list ]
y_train = [ [r[-1]] for r in data_list ]
# One hot encode [0, 1, 2] to [[1,0,0], [0,1,0], [0,0,1]]
y_one_hot = tf.keras.utils.to_categorical(y_train)

# Multinomial Classification using Tensorflow
learning_rate = 1e-2
learning_epochs = 1000

# Stochastic gradient descent (SGD) Optimizer
sgd = tf.keras.optimizers.SGD(learning_rate=learning_rate)

model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Dense(3, input_shape=(2,), activation='softmax'))

model.compile(loss='categorical_crossentropy',
              optimizer=sgd,
              metrics=['accuracy'])
print(model.summary())
# Train the model
history = model.fit(np.array(x_train), np.array(y_one_hot), epochs=learning_epochs)

plt.figure(figsize=(10,10))
plt.plot(history.history['loss'])
plt.show()

print("%20s %20s %20s" % ('학습량', '비용', '정확도')+'\n')
for step in range(learning_epochs):
    if step % 100 == 0:
        cost_val = history.history['loss'][step]
        acc_val = history.history['accuracy'][step]
        print("%20i %20.5f %20.5f" % (step, cost_val, acc_val))
        
# Prediction
Time = 10
Day = 2

time_condition = data_out['집계시'] == Time
day_condition = data_out['요일'] == Day
selected_data = data_out[time_condition & day_condition]

input = [Time, Day]
result = model.predict(np.array([input]))

grade_list = ['빠름', '보통', '느림']
grade_index = np.argmax(result[0])
grade = grade_list[grade_index]
print("%30s" % ('속도 등급')+'\n')
print("%30s" % (grade)+'\n')
print(result[0], grade_index)