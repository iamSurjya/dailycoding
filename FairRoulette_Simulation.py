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

random.seed(0)
game=FairRoulette()

for numSpins in (100,100000):
    for i in range(3):
        playRoulette(game,numSpins,2,1,True)
