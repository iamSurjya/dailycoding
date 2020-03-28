import random
class Location(object):
    def __init__(self,X,Y):
        self.X=X
        self.Y=Y
    def move(self,deltaX,deltaY):
        return Location(self.X+deltaX,self.Y+deltaY)
    def getX(self):
        return self.X
    def getY(self):
        return self.Y
    def distFrom(self,other):
        xDist=self.X-other.getX()
        yDist=self.Y-other.getY()
        return(xDist**2 + yDist**2)**0.5
    def __str__(self):
        return '<'+ str(self.X)+','+str(self.Y)+'>'

class Feild(object):
    def __init__(self):
        self.drunks={}
    def addDrunk(self,drunk,loc):
        if drunk in self.drunks:
            raise ValueError('Duplicate Error')
        else :
            self.drunks[drunk]=loc
    def moveDrunk(self,drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in Feild')
        xDist,yDist=drunk.takeStep()
        self.drunks[drunk]=self.drunks[drunk].move(xDist,yDist)
    def getLoc(self,drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in Feild')
        return self.drunks[drunk]

class Drunk(object):
    def __init__(self,name=None):
        self.name=name
    def __str__(self):
        if self!=None:
            return self.name
        return 'Anonymous'

#The 'Usual' drunk who wanders  around at  random
class UsualDrunk(Drunk):
    def takeStep(self):
        stepChoices=[(0,1),(0,-1),(1,0),(-1,0)]
        return random.choice(stepChoices)

#The 'NorthMoving' drunk who tries to move  northwards
class NorthMoving(Drunk):
    def takeStep(self):
        stepChoices=[(0.0,1.1),(0.0,0.9),(1.0,0.0),(-1.0,0.0)]
        return random.choice(stepChoices)



def walk(f,d,numSteps): #f:Feild,d:drunk, numSteps:Number of steps taken by drunks
    start=f.getLoc(d)
    for s in range(numSteps):
        f.moveDrunk(d)
    return start.distFrom(f.getLoc(d))


def simWalks(numSteps,numTrials,dClass):
    Homer=dClass('Homer')
    origin=Location(0,0)
    distance=[]
    for t in range(numTrials):
        f=Feild()
        f.addDrunk(Homer,origin)
        distance.append(round(walk(f,Homer,numSteps),1))
    return distance

def drunkTest(Walklengths,numTrials,dClass):
    for numSteps in Walklengths:
        distance=simWalks(numSteps,numTrials,dClass)
        print(dClass.__name__,'random walk of ',numSteps,'steps')
        print('Mean =',round(sum(distance)/len(distance),4))
        print('Max= ',max(distance),'Min= ',min(distance))

random.seed(0)
drunkTest((10,100,1000),100,UsualDrunk)

def simAll(drunkKinds, walkLengths, numTrials):
    for dClass in drunkKinds:
        drunkTest(walkLengths, numTrials, dClass)

simAll((UsualDrunk, NorthMoving),(1000, 10000), 100)
