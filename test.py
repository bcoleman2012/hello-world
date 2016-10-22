from matplotlib import pyplot as plt
import numpy as np
from math import pi

t = np.linspace(0,0.025,1000)
a = 2*np.cos(2*pi*60*t)
b = 2*np.cos(2*pi*60*t + 2.0/3.0*pi)
c = 2*np.cos(2*pi*60*t + 4.0/3.0*pi)

fig, ax = plt.subplots()

ax.plot(t,a,'k',label = "P1")
ax.plot(t,b,'b',label = "P2")
ax.plot(t,c,'r',label = "P3")

ax.set_xlim(0,0.025)

plt.title("Three-Phase Power")
ax.set_xlabel("Time (sec)")
ax.set_ylabel("Voltage (V)")

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels,loc=1)

plt.show()