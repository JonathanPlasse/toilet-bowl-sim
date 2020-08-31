import numpy as np
import matplotlib.pyplot as plt

def R(t):
    return np.array([[np.cos(t),np.sin(t)],[-np.sin(t),np.cos(t)]])

def r(theta, r0, t, p, rs0, v):
    return np.exp(-t*p*np.cos(theta))*R(-t*p*np.sin(theta)).dot(r0-rs0+R(-theta).dot(v/p))+rs0+v*t-R(-theta).dot(v/p)

def plot_tb(r0, rs0, v):
    r_t = np.array([r(theta, r0, t_i, p, rs0, v) for t_i in t])
    plt.plot(r_t[:,0],r_t[:,1])

t_final = 10
n = 1000
r0 = np.array([0,0])

for j, p in enumerate(np.linspace(0.04, 2, 50)):
    for deg in range(10, 100, 10):
        theta = deg*np.pi/180
        t = [i/(n-1)*t_final for i in range(n)]

        rs0 = np.array([t_final,0])
        v = np.array([0,0])
        plot_tb(r0, rs0, v)


        # rs0 = np.array([0,0])
        # v = np.array([1,0])
        # plot_tb(r0, rs0, v)

    plt.axis('equal')
    plt.xlim(-5, 25)
    plt.ylim(-15, 15)
    plt.title('Toilet Bowl Échelon p={:.2f}'.format(p))

    plt.savefig('tb_ramp_p'+str(j).zfill(2))
    plt.cla()