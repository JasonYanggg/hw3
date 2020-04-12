import matplotlib.pyplot as plt
import numpy as np
import serial
import time

t = np.arange(0, 10, 0.1)
x = np.arange(0, 1, 0.01)
y = np.arange(0, 1, 0.01)
z = np.arange(0, 1, 0.01)
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
    tilt[i] = int(line)
    
fig, ax = plt.subplots(2, 1)
ax[0].plot(t, x, color='blue', linewidth=1, linestyle='-', label='x')
ax[0].plot(t, y, color='red', linewidth=1, linestyle='-', label='y')
ax[0].plot(t, z, color='green', linewidth=1, linestyle='-', label='z')
ax[0].legend(loc='lower left')
ax[0].set_xlabel('Time')
ax[0].set_ylabel('Acc Vector')
ax[1].stem(t, tilt)
ax[1].set_xlabel('Time')
ax[1].set_ylabel('Tilt')
plt.show()
s.close()
