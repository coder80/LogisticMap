import logmap as lg
import logmapn as lmn
import numpy as np
import os
import matplotlib.pyplot as plt
import numpy as np
import lyapunov as lp


class PolyMap:
    def __init__(self, iterations=1, coeffs=[3.58]):
        self.numMaps = len(coeffs)
        self.iterations = iterations
        self.logMaps = []
        for c in coeffs:
            self.logMaps.append(lg.LogMap(c, iters=self.iterations))

    def calc(self, x):
        x0 = x
        for m in self.logMaps:
            x0 = m.calc(x0)
        return x0

class PolyMapN:
    def __init__(self):
        pass

    def calc(self):
        r = 3.68
        np.fill(3, 0.1)
        X = np.arange(0., 1., 0.01)
        lgmap = lmn.LogMapN(r, 3, 10)
        for x in X:
            y = lgmap.calc(x)
def main():
    coeff = np.arange(3.68, 4.0, 0.01)
    coeffrnd = np.random.uniform(low=3.58, high=4., size=(len(coeff),))
    X = np.arange(0., 1., 0.01)
    m = PolyMap(3, coeff)
    mrnd = PolyMap(1, coeffrnd)
    m0 = PolyMap(20, [3.68])
    Y = []
    YR = []
    Y0 = []
    for x in X:
        Y.append(m.calc(x))
        #YR.append(mrnd.calc(x))

    fig = plt.figure()
    plt.plot(X, Y)
    #plt.plot(X, YR)
    plt.show()

if __name__ == "__main__":
    main()