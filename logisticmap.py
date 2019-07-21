class LogisticMap:
    def __init__(self, r, x0):
        self.r = r
        self.x = x0
        self.x0 = x0

    def logistic(self):
        self.x = self.r * self.x * (1. - self.x)
        return self.x

    def logistic_d(self, x):
        dx = self.r * (1. - 2 * x)
        return dx