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
        self.value = 0


    def addRule(self, f1, f2, of):
        self.ruleSet.append(self.Rule(f1,f2,of))

    def doInference(self, _i1, _i2):
        c = []
        for r in self.ruleSet:
            a = r.getA(_i1,_i2)
            c.append(r.f1.centroid(a))
        
        
        sum = [0,0]
        for j in c:
            sum[0] += j[0]*j[1]
            sum[1] += j[1]

        print(sum[0] , sum[1])
        if int(sum[1]) == 0:
            return 0
        self.value = int(sum[1]) == 0 and 0 or (sum[0] / sum[1])
        return self.value

    def doAction(self):
        return self.value > 0.0 and 'Raining' or 'Not Rain'



if __name__ == '__main__':
    pass