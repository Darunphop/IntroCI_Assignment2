import fuzzyClothline
import fuzzy
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # fc = fuzzyClothline.Clothline()
    # fBright = fuzzy.fuzzy([[0.0,0.0],[700.0,0.0],[1000.0,1.0]])
    # fDark = fuzzy.fuzzy([[0.0,1.0],[300.0,1.0],[700.0,0.0]])
    # fWet = fuzzy.fuzzy([[0.0,0.0],[60.0,0.0],[100.0,1.0]])
    # fDry = fuzzy.fuzzy([[0.0,1.0],[50.0,1.0],[100.0,0.0]])

    # fLow = fuzzy.fuzzy([[-2.5,0],[-1,1.0],[0.0,0.0]])
    # fMedium = fuzzy.fuzzy([[-0.5,0],[0.0,1.0],[0.5,0.0]])
    # fHigh = fuzzy.fuzzy([[0.0,0.0],[1.0,1.0],[3.5,0.0]])


    # fc.addRule(fBright,fWet,fMedium)
    # fc.addRule(fBright,fDry,fLow)
    # fc.addRule(fDark,fWet,fHigh)
    # fc.addRule(fDark,fDry,fMedium)

    # wx = [0,500,1000,1500]
    # wy = [0,0,1,1]
    # dx = [0,300,800,1500]
    # dy = [1,1,0,0]

    x = [-2.5,-0.5,-1,0,0.5,1,3.5]
    ax = [-2.5,-1,0]
    bx = [-0.5,0,0.5]
    cx = [0,1,3.5]
    y = [0,1,0]

    fig = plt.figure(1)
    plt.title('Memnbership of Output')
    plt.plot(ax, y, 'go-',label='Low', ms=5)
    plt.plot(bx, y, 'bo-',label='Middle', ms=5)
    plt.plot(cx, y, 'ro-',label='High', ms=5)
    plt.legend(loc='best')
    fig.savefig('out.png')
    # w = np.arange(10,110, 10)
    # l = np.arange(100,1100, 100)
    # res = []

    # fig = plt.figure(1)
    # plt.title('Result')
    # plt.xlabel('Humidity')
    # plt.ylabel('Brightness')
    # for i in range(10):
    #     for j in range(10):
    #         fc.doInference(l[i],w[j])
    #         # res.append(fc.doAction())
    #         if fc.doAction() == 'Raining':
    #             plt.plot(j*10, i*100, 'ro', ms=5)
    #         else:
    #             plt.plot(j*10, i*100, 'bo', ms=5)

    # fig.savefig('exp1,'+str((i+1))+'.png')
