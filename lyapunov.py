import math
def lyapunov(x):
    l = 0.
    for k in x:
        l += math.log2(math.fabs(k))
    N = len(x)
    l = l / N
    return l