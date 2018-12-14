import numpy as np

class Lightness:

    def __init__(self, _lumen):
        self.lumen = _lumen
        self.fHowBright = np.vectorize(self.howBright)
        self.fHowDark = np.vectorize(self.howDark)

    def howBright(self, _lumen=[]):
        if len(_lumen) == 0:
            _lumen = self.lumen
        return max(0.0, min(1.0, (_lumen - 400.0)/(1000.0 - 400.0)))

    def howDark(self, _lumen):
        if len(_lumen) == 0:
            _lumen = self.lumen
        return max(0.0,min(1.0, 1.0 - (_lumen - 400.0)/(600.0 - 400.0)))

if __name__ =='__main__':
    
    x = np.arange(500,1000)
    l = Lightness(x)
    # print(list(x))
    y = np.asarray([555,666,789])
    print(l.fHowBright())
    print(l.fHowBright(y))
    print(l.fHowDark())