import pandas as pd
import matplotlib.pyplot as plt
import math
import numpy as np
import matplotlib.animation as animation
from matplotlib import rc

# Tortoise and Hare
# 상수 설정
Hare_Speed = 2
MAXVAL = 10
INTERVAL = MAXVAL + 1
h_xdata, h_ydata = [],[]

# Configure figure size
plt.figure(figsize=(5,5))

for t in np.linspace(0, MAXVAL, INTERVAL):
    h_y = Hare_Speed*t
    h_xdata.append(t)
    h_ydata.append(h_y)

plt.plot(h_xdata, h_ydata, 'ro', label='Hare')

plt.title('Linear Regression', fontsize=16)
plt.xlabel('Time(hour)', fontsize=14)
plt.ylabel('Distance(km)', fontsize=14)
plt.legend()
#Show plot
plt.show()

# Hypothesis
Velocity_Variance = 0.2
LINES = 5
# Configure figure size
plt.figure(figsize=(5,5))
# a_val = 3
a_val = Hare_Speed + (Velocity_Variance * LINES)
h_xdata, h_ydata, v_xdata, v_ydata = [], [], [], []

for t in np.linspace(0, MAXVAL, INTERVAL):
    h_y = Hare_Speed*t
    h_xdata.append(t)
    h_ydata.append(h_y)
    # a는 속도 : 최대 3에서 0.2 씩 줄어든다.
    a = a_val - (t * Velocity_Variance)
    for i in np.linspace(0, MAXVAL, INTERVAL):
      h_y = a * i
      v_xdata.append(i)
      v_ydata.append(h_y)
    # 각 점을 이어서 선 그래프를 그린다.
    plt.plot(v_xdata, v_ydata, alpha=0.2)

plt.plot(h_xdata, h_ydata, 'ro', label='Hare')

plt.title('Linear Regression', fontsize=16)
plt.xlabel('Time(hour)', fontsize=14)
plt.ylabel('Distance(km)', fontsize=14)
plt.legend()
#Show plot
plt.show()

# Cost : Gradient Descent
rc('animation', html='jshtml')

# Configure figure size
fig = plt.figure(figsize=(5,5))
# 111은 옵션 중의 하나.
ax = fig.add_subplot(111)
# set x limit 0 ~ 2
ax.set_xlim(-0.1, 2.1)
# set y limit 0 ~ 400
ax.set_ylim(0, 400)
t_xdata, t_ydata = [], []
# Squared Error
def get_cost(a_val):
  cost = 0
  for i in np.linspace(0, MAXVAL, INTERVAL):
    # 선과 점 사이 거리의 제곱 값을 구하는 공식
    # pow(,2) : 제곱값을 구하는 함수
    cost += pow((a_val*i - Hare_Speed*i), 2)
  return cost

def animateFrame(frame):
  a_val = Hare_Speed + (Velocity_Variance * LINES)
  i = frame * Velocity_Variance
  a = a_val - i
  t_xdata.append(i)
  t_ydata.append(get_cost(a))
  plot = ax.plot(t_xdata, t_ydata, 'ro')
  return plot

# animation객체를 생성
anim = animation.FuncAnimation(fig, animateFrame, frames=np.linspace(0, MAXVAL, INTERVAL), blit=True, repeat=False)
ax.set_title('Gradient Descent')
ax.set_ylabel('Total Cost')
ax.set_xlabel('Variance')
# Show Animation
anim
