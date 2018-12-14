import lightness
import wetness
import fuzzy

class Clothline:
    class Rule:
        def __init__(self, _f1, _f2, _o):
            self.f1 = _f1
            self.f2 = _f2
            self.fo = _o

        def getA(self, _i1, _i2):
            return self.fo.getAlphaCut(min(self.f1.getMemberness(_i1), self.f2.getMemberness(_i2)))

    def __init__(self):
        self.ruleSet = []


    def addRule(self, f1, f2, of):
        self.ruleSet.append(f1,f2,of)

if __name__ == '__main__':
    pass