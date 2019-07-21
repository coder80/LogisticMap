import logisticmap as lg
import os
import matplotlib.pyplot as plt
import numpy as np
import lyapunov as lp

def lyapunov_map(r, x0, iterations):
    ret = []
    for rr in r:
        map = lg.LogisticMap(rr, x0)
        lm = [map.logistic() for i in range(0, iterations)]
        dlm = [map.logistic_d(lm[i]) for i in range(0, iterations)]
        l = lp.lyapunov(dlm)
        ret.append(l)
    return ret

rr = 3.99999 #3.58
rr1 = 3.58
x0 = 0.1
map_s = lg.LogisticMap(1.1, x0)
map = lg.LogisticMap(3.1,x0)
map_chaotic = lg.LogisticMap(rr, x0)
map_chaotic_second = lg.LogisticMap(rr, x0)
map_chaotic_1 = lg.LogisticMap(rr, x0)
map_chaotic_2 = lg.LogisticMap(rr1, x0)

iterations = 1000

lms = [map_s.logistic() for i in range(0, iterations)]
lm = [map.logistic() for i in range(0, iterations)]
lmc = [map_chaotic.logistic() for i in range(0, iterations)]
lmc1 = [(map_chaotic_2.logistic()) for i in range(0, iterations)]
lmc_second = [map_chaotic_second.logistic() for i in range(0, iterations)]

X = range(0, iterations)

dlmc = [map_chaotic.logistic_d(lmc[i]) for i in range(0, iterations)]
lpc = lp.lyapunov(dlmc)
print(lpc)

print(lmc[-1])
print(lmc_second[-1])

r = np.arange(3.5, 4., 0.001)
lp_map = lyapunov_map(r, 0.1, 1000)

fig = plt.figure()
plt.plot(X, lmc)
plt.plot(X, lms)
plt.plot(X, lm)
plt.plot(X, lmc1)

fig1 = plt.figure()
plt.plot(r, lp_map)
plt.show()

