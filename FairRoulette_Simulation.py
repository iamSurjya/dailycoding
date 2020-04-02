import random

class FairRoulette():
    def __init__(self):
        self.pockets=[]
        for i in range(1,37): #Assuming a Roulette with 36 pockets
            self.pockets.append(i)
        self.ball=None
        self.pocketsOdds=len(self.pockets)-1
    def spin(self):
        self.ball=random.choice(self.pockets)
    def betPocket(self,pocket,amt):
        if str(pocket)==str(self.ball):
            return amt*self.pocketsOdds
        else:
            return -amt
    def __str__(self):
        return 'Fair Roulette'

def playRoulette(game,numSpins,pocket,bet,toPrint):
    totpocket=0
    for i in range(numSpins):
        game.spin()
        totpocket+=game.betPocket(pocket,bet)
    if toPrint:
        print(numSpins,'spine of ', game)
        print('Expected return betting',pocket,'=',str(100*totpocket/numSpins)+'%\n')
    return (totpocket/numSpins)

class EuRoulette(FairRoulette):
    def __init__(self):
        FairRoulette.__init__(self)
        self.pockets.append('0')
    def __str__(self):
        return 'European Roulette'

class AmRoulette(EuRoulette):
    def __init__(self):
        EuRoulette.__init__(self)
        self.pockets.append('00')
    def __str__(self):
        return 'American Roulette'

def findPocketReturn(game,numTrials,trialsize,toPrint):
    pocketReturn=[]
    for t in range(numTrials):
        trialVals=playRoulette(game,trialsize,2,1,toPrint)
        pocketReturn.append(trialVals)
    return pocketReturn

random.seed(0)
numTrials = 20
resultDict = {}

games={FairRoulette,EuRoulette,AmRoulette}
for G in games:
    resultDict[G().__str__()]=[]
for numSpins in (1000,10000,100000,1000000):
    print('\nSimulate', numTrials, 'trials of',numSpins, 'spins each')
    for G in games:
        pocketReturn =findPocketReturn(G(),numTrials,numSpins,False)
        expReturn=100*sum(pocketReturn)/len(pocketReturn)
        print('Exp. return for', G(), '=',str(round(expReturn, 4)) + '%')
