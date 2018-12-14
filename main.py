import fuzzyClothline
import fuzzy

if __name__ == '__main__':
    fc = fuzzyClothline.Clothline()
    fBright = fuzzy.fuzzy([[400.0,0.0],[1000.0,1.0]])
    fDark = fuzzy.fuzzy([[400.0,1.0],[600.0,0.0]])
    fWet = fuzzy.fuzzy([[60.0,0.0],[100.0,1.0]])
    fDry = fuzzy.fuzzy([[50.0,1.0],[100.0,0.0]])

    fLow = fuzzy.fuzzy([[-2.0,0],[-1,1.0],[0.0,0.0]])
    fMedium = fuzzy.fuzzy([[-1.0,0],[0.0,1.0],[1.0,0.0]])
    fHigh = fuzzy.fuzzy([[0.0,0.0],[1.0,1.0],[2.0,0.0]])

    fc.addRule(fBright,fWet,fMedium)
    fc.addRule(fBright,fDry,fLow)
    fc.addRule(fDark,fWet,fHigh)
    fc.addRule(fDark,fDry,fMedium)

