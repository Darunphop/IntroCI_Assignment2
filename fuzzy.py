import numpy as np

class fuzzy:
    def __init__(self, _membership=[]):
        self.membership = _membership

    def getMemberness(self, val):
        res = 0
        for i in range(len(self.membership)):
            if val <= self.membership[i][0]:
                if i == 0:
                    res = self.membership[i][1]
                    break
                else:

                    res = (self.membership[i][0] > self.membership[i-1][0] and 0 or 1) - (val - self.membership[i-1][0])/(self.membership[i][0]-self.membership[i-1][0])
                    break
            elif i == len(self.membership[i])-1:
                res = self.membership[i][1]
        return res

    def getAlphaCut(self, val):
        res = []
        for i in range(len(self.membership)-1):
            if self.membership[i][1] < val and self.membership[i+1][1] > val:
                res.append(self.membership[i])
                res.append([val*(self.membership[i+1][0]-self.membership[i][0])+self.membership[i][0],val])
                # print('A')

            elif self.membership[i][1] > val and self.membership[i+1][1] < val:
                res.append([self.membership[i][0],val])
                res.append([(1-val)*(self.membership[i+1][0]-self.membership[i][0])+self.membership[i][0], val])
                # print('b')
                
            elif self.membership[i][1] < val:
                res.append(self.membership[i])
                # print('c')
            elif self.membership[i][1] >= val:
                res.append([self.membership[i][0],val])
                # print('d')

        if self.membership[-1][1] < val:
            res.append(self.membership[-1])
            # print('e')
        else:
            res.append([self.membership[-1][0],val])
            # print('f')

        return res

    def getCentroid(self):
        return self.centroid(self.membership)
    
    def centroid(self, _mem):
        c = []
        matter = 0.0
        for i in range(len(_mem)-1):
            if _mem[i][0] < _mem[i+1][0]:
                tmp = [_mem[i][0]+((_mem[i+1][0]-_mem[i][0])*(2.0/3.0)), _mem[i+1][1]/3.0]
                c.append(tmp)
                # matter += 0.5*(_mem[i+1][0]-_mem[i][0])*_mem[i+1][1]
            elif _mem[i][0] > _mem[i+1][0]:
                tmp = [_mem[i][0]+((_mem[i+1][0]-_mem[i][0])*(1.0/3.0)), _mem[i+1][1]/3.0]
                c.append(tmp)
                # matter += 0.5*(_mem[i+1][0]-_mem[i][0])*_mem[i][1]
            else:
                tmp = [_mem[i][0]+((_mem[i+1][0]-_mem[i][0])/2.0), _mem[i][1]/2.0]
                # matter += (_mem[i+1][0]-_mem[i][0])*_mem[i+1][1]

        sum = [0,0]
        for j in c:
            sum[0] += j[0]*j[1]
            sum[1] += j[1]
            print(j[0], j[1])
            matter += j[1]

        return sum[1]==0 and [0,0] or [sum[0] / sum[1], matter]
            

if __name__ == '__main__':
    w = fuzzy([[400,0.0],[1000,1.0]])
    d = fuzzy([[400,1],[600,0]])
    print(w.getAlphaCut(0.5))
    print(d.getAlphaCut(0.5))
    w.membership = w.getAlphaCut(0.5)
    print(w.getCentroid())