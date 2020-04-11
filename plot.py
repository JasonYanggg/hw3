import matplotlib.pyplot as plt
import numpy as np
import serial
import time

t = np.arange(0, 10, 0.1)
x = np.arange(100)
y = np.arange(100)
z = np.arange(100)
tilt = np.arange(100)

serdev = '/dev/ttyACM0'
s = serial.Serial(serdev)

for i in range(100):
    line = s.readline()
    x[i] = float(line)
    line = s.readline()
    y[i] = float(line)
    line = s.readline()
    z[i] = float(line)
    line = s.readline()
    tilt[i] = float(line)
    
fig, ax = plt.subplots(2, 1)
ax[0].plot(t, x)
ax[0].plot(t, y)
ax[0].plot(t, z)
ax[1].plot(t, tilt)
plt.show()
s.close()