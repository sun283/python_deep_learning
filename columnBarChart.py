# This code is working on google colab
# needs to be altered using pydrive
# Mount Drive
# from google.colab import drive
# drive.mount('/gdrive')
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load a file under "data" folder
file = "/gdrive/My Drive/data/data_2021.csv"
data = pd.read_csv(file)

data_2PM = data[data.집계시 == 14]
plt.figure(figsize = (20,10))
plt.rc('font', family='NanumBarunGothic')

# 세로 막대 그래프
data_2PM_Destination = sns.countplot('도착영업소코드', data=data_2PM)
data_2PM_Destination.set_title('통행횟수 by 도착영업소', fontsize = 18)
data_2PM_Destination.set_xlabel('도착영업소', fontdict={'size':16})
data_2PM_Destination.set_ylabel('통행횟수', fontdict={'size':16})
plt.show()

# 가로 막대 그래프
data_2PM_Destination = sns.countplot(y='도착영업소코드', data=data_2PM)
data_2PM_Destination.set_title('통행횟수 by 도착영업소', fontsize = 18)
data_2PM_Destination.set_xlabel('통행횟수', fontdict={'size':16})
data_2PM_Destination.set_ylabel('도착영업소', fontdict={'size':16})
plt.show()

# Hue Data
data_2PM_Destination = sns.countplot('도착영업소코드', data=data_2PM, hue='요일')
data_2PM_Destination.set_title('통행횟수 by 도착영업소', fontsize = 18)
data_2PM_Destination.set_xlabel('도착영업소', fontdict={'size':16})
data_2PM_Destination.set_ylabel('통행횟수', fontdict={'size':16})
plt.show()