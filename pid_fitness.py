import numpy as np
from scipy.signal import find_peaks

def pid1_fitness(Kp, Ti, Td, T=1):
    try: 
        q0 = Kp*(1 + T/Ti + Td/T)
        q1 = -Kp*(1 + 2*Td/T)
        q2 = Td*Kp / T

        b1 = 1
        b2 = 0.5
        a1 = -1.5
        a2 = 0.7

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

        steady_state_error = np.abs(y[-1] - 1)
        peaks, _ = find_peaks(y)   

        rise_time = peaks[0]*T
        overshoot_idx = np.argmax(y)
        overshoot = (y[overshoot_idx] - 1)*100
        delay = peaks[-1]*T
        score = 1 / ((steady_state_error + 1e-6)*(rise_time + 1e-6)*(overshoot + 1e-6)*(delay + 1e-6))
        return score
    
    except:
        return -1e20
        
def pid2_fitness(Kp, Ti, Td, T=1):
    try: 
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
            

        steady_state_error = np.abs(y[-1] - 1)
        peaks, _ = find_peaks(y)   

        rise_time = peaks[0]*T
        overshoot_idx = np.argmax(y)
        overshoot = (y[overshoot_idx] - 1)*100
        delay = peaks[-1]*T
        score = 1 / ((steady_state_error + 1e-6)*(rise_time + 1e-6)*(overshoot + 1e-6)*(delay + 1e-6))
        return score
    
    except:
        return -1e20

def pid3_fitness(Kp, Ti, Td, T=1):
    try: 
        q0 = Kp*(1 + T/Ti + Td/T)
        q1 = -Kp*(1 + 2*Td/T)
        q2 = Td*Kp / T

        b1 = 0.00462
        b2 = 0.00169
        b3 = -0.00273
        a1 = -2.48824
        a2 = 2.05387
        a3 = -0.56203

        step_num = 100

        e = np.zeros(step_num)
        u = np.zeros(step_num)
        y = np.zeros(step_num)
        du = np.zeros(step_num)

        for k in range(step_num):
            e[k] = 1 - y[k-1]
            du[k] = q0*e[k] + q1*e[k-1] + q2*e[k-2]
            u[k] = du[k] + u[k-1]
            y[k] = b1*u[k-1] + b2*u[k-2] + b3*u[k-3] - (a1*y[k-1] + a2*y[k-2]+ a3*y[k-3]) 

        steady_state_error = np.abs(y[-1] - 1)
        peaks, _ = find_peaks(y)   

        rise_time = peaks[0]*T
        overshoot_idx = np.argmax(y)
        overshoot = (y[overshoot_idx] - 1)*100
        delay = peaks[-1]*T
        score = 1 / ((steady_state_error + 1e-6)*(rise_time + 1e-6)*(overshoot + 1e-6)*(delay + 1e-6))
        return score
    
    except:
        return -1e20


if __name__ == '__main__':
    # print(pid1_fitness(0.07, 4.804, 4.63, 2))
    print(pid3_fitness(2.9556870827270654, 18.62385932338612, 4.868346929787249))

