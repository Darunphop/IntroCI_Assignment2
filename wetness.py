import numpy as np

class Wetness:

    def __init__(self, _humid):
        self.humid = _humid
        self.fHowWet = np.vectorize(self.howWet)
        self.fHowDry = np.vectorize(self.howDry)

    def howWet(self, _humid):
        return max(0.0, min(1.0, (_humid - 60.0)/(100.0 - 60.0)))

    def howDry(self, _humid):
        return max(0.0,min(1.0, 1.0 - (_humid - 50.0)/(100.0 - 50.0)))

if __name__ =='__main__':
    
    x = np.arange(10,110)
    w = Wetness(list(x))
    # print(list(x))
    y = np.asarray([40,66,90])
    # print(h.how)
    print(w.fHowWet(w.humid))
    print(w.fHowWet(y))
    print(w.fHowDry(w.humid))