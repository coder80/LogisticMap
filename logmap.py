class LogMap:
    def __init__(self, r, iters=1):
        self.r = r
        self.iters = iters

    def calc(self, x):
        ret = x
        for i in range(1, self.iters + 1):
            ret = self.r * ret * (1. - ret)
        return ret

    def calcDiff(self, x):
        return self.r * (1 - 2 * x)


class LogMapPow:
    def __init__(self, r, iters=1, l=1):
        self.r = r
        self.iters = iters
        self.l = l

    def calc(self, x):
        ret = x
        for i in range(1, self.iters + 1):
            ret = self.r * pow(ret, self.l) * (1. - pow(ret, self.l))
        return ret

    def calcDiff(self, x):
        return self.r * (1 - 2 * x)


class LogMapAB:
    def __init__(self, r, iters=1, a=1, b=2):
        self.r = r
        self.iters = iters
        self.a = a
        self.b = b

    def calc(self, x):
        ret = x
        for i in range(1, self.iters + 1):
            ret = self.r * pow(ret, self.a) * (1. - pow(ret, self.b))
        return ret

    def calcDiff(self, x):
        return self.r * (1 - 2 * x)
