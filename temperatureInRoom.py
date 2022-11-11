from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
def model(T,t,k0):
    k1 = 1
    k2 = 1
    Ta = 25
    dTdt = k0*(T - Ta) #Newton's law of cooling
    return dTdt

k0 = [-2, 0, 1] #positive if trying to heat up room and negative if not
t = np.linspace(0,20,200)
result = odeint(model,k0,t,args=(k0,))

fig,ax = plt.subplots()
ax.plot(t,result[:,0],label='k0=-1')
ax.plot(t,result[:,1],label='k0=0')
ax.plot(t,result[:,2],label='k0=1')
ax.legend()
ax.set_xlabel('t')
ax.set_ylabel('T')
plt.show()