import numpy as np
import matplotlib.pyplot as plt

Kp = 1.1612011971293679
Ti = 13.332589985710797
Td = 2.727725324992248
T = 1

q0 = Kp*(1 + T/Ti + Td/T)
q1 = -Kp*(1 + 2*Td/T)
q2 = Td*Kp / T

b1 = -0.07289
b2 = 0.09394
a1 = -1.68364
a2 = 0.70469

step_num = 100

e = np.zeros(step_num)
u = np.zeros(step_num)
y = np.zeros(step_num)
du = np.zeros(step_num)

for k in range(step_num):
    e[k] = 1 - y[k-1]
    du[k] = q0*e[k] + q1*e[k-1] + q2*e[k-2]
    u[k] = du[k] + u[k-1]
    y[k] = b1*u[k-1] + b2*u[k-2] - (a1*y[k-1] + a2*y[k-2])

t = np.linspace(start=0, stop=step_num-1, num=step_num, dtype=int)

plt.subplot(2,2,1)
plt.plot(t, y)
plt.xlabel('t')
plt.ylabel('y')
plt.title('y(k)')

plt.subplot(2,2,2)
plt.plot(t, u)
plt.xlabel('t')
plt.ylabel('u')
plt.title('u(k)')

plt.subplot(2,2,3)
plt.plot(t, du)
plt.xlabel('t')
plt.ylabel('du')
plt.title('du(k)')

plt.subplot(2,2,4)
plt.plot(t, e)
plt.xlabel('t')
plt.ylabel('e')
plt.title('e(k)')

plt.show()
