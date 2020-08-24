import numpy as np
import pyqtgraph as pg

def R(t):
    return np.array([[np.cos(t),np.sin(t)],[-np.sin(t),np.cos(t)]])

def r(theta, r0, t, p, rs0, v):
    return np.exp(-t*p*np.cos(theta))*R(-t*p*np.sin(theta)).dot(r0-rs0+R(-theta).dot(v/p))+rs0+v*t-R(-theta).dot(v/p)

def plot_tb(r0, rs0, v):
    r_t = np.array([r(theta, r0, t_i, p, rs0, v) for t_i in t])
    plt.plot(r_t[:,0],r_t[:,1])

theta = 80*np.pi/180
t_final = 10
p = 1
n = 1000
r0 = np.array([0,0])

t = [i/(n-1)*t_final for i in range(n)]

plt = pg.PlotWindow()
plt.setAspectLocked()

rs0 = np.array([10,0])
v = np.array([0,0])
plot_tb(r0, rs0, v)

rs0 = np.array([0,0])
v = np.array([1,0])
plot_tb(r0, rs0, v)

