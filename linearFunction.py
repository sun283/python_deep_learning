import pandas as pd
import matplotlib.pyplot as plt
import math
import numpy as np

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

