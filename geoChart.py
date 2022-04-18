# This code is working on google colab
# needs to be altered using pydrive
# Mount Drive
# from google.colab import drive
# drive.mount('/gdrive')
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import folium
# Import folium : https://python-visualization.github.io/folium/

plt.rc('font', family='NanumBarunGothic')
# Load a file under "data" folder
file = "/gdrive/My Drive/data/data_2021.csv"
data = pd.read_csv(file)

# Bubble CHart, 도착영업소코드
data_destination_mean = data.groupby(by='도착영업소코드').mean()
data_destination_mean_time = data_destination_mean['통행시간']
data_destination_count = data.groupby(by='도착영업소코드').count()
data_destination_count_time = data_destination_count['통행시간']
x = data_destination_mean_time.index
# 101 서울, 105 기흥, 110 목천, 115 대전, 120 황간, 125 남구미, 130 동김천, 135 경주, 140 부산
labels = ['기흥', '목천', '대전', '황간', '남구미', '동김천', '경주', '부산']
values = data_destination_mean_time.values
counts = data_destination_count_time.values
colors = np.random.rand(len(labels))

plt.figure(figsize=(20,10))
# Create Bubble Chart
plt.scatter(labels, values, s=counts, c=colors, alpha=0.5)
for i, txt in enumerate(counts):
  plt.annotate(txt, (labels[i], values[i]), fontsize=14)
plt.title('도착영업소 기준 통행회수', fontsize=18)
plt.xlabel('도착영업소', fontdict={'size':16})
plt.ylabel('통행회수', fontdict={'size':16})
# Show plot
plt.show()

# Geo Chart
locations = [
            {"code": 105, "name": "기흥", "long": 127.102439, "lat": 37.222249},
            {"code": 110, "name": "목천", "long": 127.230613, "lat": 36.768046},
            {"code": 115, "name": "대전", "long": 127.448328, "lat": 36.361320},
            {"code": 120, "name": "황간", "long": 127.901970, "lat": 36.223015},
            {"code": 125, "name": "남구미", "long": 128.371780, "lat": 36.072653},
            {"code": 130, "name": "동김천", "long": 128.175000, "lat": 36.140000},
            {"code": 135, "name": "경주", "long": 129.188771, "lat": 35.809907},
            {"code": 140, "name": "부산", "long": 129.105170, "lat": 35.278705}
        ] 

idx = 1
location = locations[idx]
folium.Map(location=[location['lat'], location['long']])

folium.Map(location=[location['lat'], location['long']],
           tiles='Stamen Toner', # "Stamen Terrain", "cartodbpositron"
           zoom_start=13
    )

#---------------------------------------------------------------------------------------
map = folium.Map(location=[location['lat'], location['long']],
           tiles='Stamen Terrain', # "Stamen Toner", "cartodbpositron"
           zoom_start=13
    )
popup = str(location['code']) + '. ' + location['name']
folium.Marker([location['lat'], location['long']],
              popup=popup, tooltip=location['code'],
              icon=folium.Icon(color='red', icon='info-sign')).add_to(map)

#---------------------------------------------------------------------------------------
max_radius = 50
radius = int(max_radius * counts[idx]/counts.max())
color = 'green'
map = folium.Map(location=[location['lat'], location['long']],
           tiles='cartodbpositron', # "Stamen Toner", "Stamen Terrain"
           zoom_start=8
    )
popup = location['name'] + ' : ' + str(counts[idx])
folium.CircleMarker([location['lat'], location['long']],
                    radius=radius, color=color, fill=True, fill_corlor=color, popup=popup).add_to(map)

#---------------------------------------------------------------------------------------
max_radius = 50
color='green'
# 함수 생성
def putCircle(idx):
  location = locations[idx]
  radius = int(max_radius * counts[idx] / counts.max())
  popup = location['name'] + ' : ' + str(counts[idx])
  folium.CircleMarker([location['lat'], location['long']],
                    radius=radius, color=color, fill=True, fill_corlor=color, popup=popup).add_to(map)

# 지도 중간의 위치를 설정 : 중간 값의 위도, 경도를 설정한다
center = int(len(locations) / 2)
map = folium.Map(location=[locations[center]['lat'], locations[center]['long']],
           tiles='cartodbpositron', # "Stamen Toner", "Stamen Terrain"
           zoom_start=8
    )
# for loop를 돌면서 해당 좌표에 동그라미를 그린다.
for i in range(len(locations)):
  putCircle(i)