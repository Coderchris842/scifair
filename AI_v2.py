import random
mcs = int(input("Max Links:"))
class AI:
    games = 0
    BetrayMarker = 50
    MarkerMod = 1
    Wins = 0
    prevwins = 0
    name = 'AI'
    control = False
    links = []
    def __init__(self, name):
        self.name = name
        self.links = []
        self.BetrayMarker = 50
        self.Wins = 0
        self.prevwins = 0
        self.MarkerMod = 1
    def cws(self, years):
        if years < 2:
            self.prevwins = self.Wins
            self.Wins += 1
            if self in self.links:
                raise NameError
        else:
            self.prevwins = self.Wins
            self.Wins =- 1
    def update(self, sults, choice, part):
        ##(self.links)
        self.games += 1
        ##(self.links)
        if part == self:
            ##(self.links)
            ##("dude")
            raise TabError
        if self in self.links:
            ##(self.links)
            ##("dudes")
            raise ValueError
        if part in part.links:
            ##(self.links)
            ##("dudes")
            raise ValueError
        if not part.control:
            ##(self.links)
            if not part in self.links:
                ##(self.links)
                if len(self.links) < mcs:
                    ##(self.links)
                    if part in part.links:
                        ##(self.links)
                        ##("dudes")
                        raise ValueError
                    self.links.append(part)
                    if part in part.links:
                        ##(self.links)
                        ##("dudes")
                        raise ValueError
                    ##(self.links)
            else:
                ##(self.links)
                if len(self.links) == mcs:
                    ##(self.links)
                    self.links.remove(part)
                    ##(self.links)
            if part in part.links:
                ##(self.links)
                ##("dudes")
                raise ValueError
        if sults == 0:
            if choice == 2:
                self.BetrayMarker = self.BetrayMarker - 2
            elif choice == 1:
                self.BetrayMarker = self.BetrayMarker + 2
        elif sults == 1:
            if choice == 2:
                self.BetrayMarker = self.BetrayMarker - 1
            elif choice == 1:
                self.BetrayMarker = self.BetrayMarker + 1
        elif sults == 2:
            if choice == 2:
                self.BetrayMarker = self.BetrayMarker + 1
            elif choice == 1:
                self.BetrayMarker = self.BetrayMarker - 1
        elif sults == 3:
            if choice == 2:
                self.BetrayMarker = self.BetrayMarker + 2
            elif choice == 1:
                self.BetrayMarker = self.BetrayMarker - 2
        if self.BetrayMarker > 100:
            self.BetrayMarker = 100
        elif self.BetrayMarker < 0:
            self.BetrayMarker = 0
        for i in self.links:
            if sults == 0:
                if choice == 2:
                    i.BetrayMarker = i.BetrayMarker - 2
                elif choice == 1:
                    i.BetrayMarker = i.BetrayMarker + 2
            elif sults == 1:
                if choice == 2:
                    i.BetrayMarker = i.BetrayMarker - 1
                elif choice == 1:
                    i.BetrayMarker = i.BetrayMarker + 1
            elif sults == 2:
                if choice == 2:
                    i.BetrayMarker = i.BetrayMarker + 1
                elif choice == 1:
                    i.BetrayMarker = i.BetrayMarker - 1
            elif sults == 3:
                if choice == 2:
                    i.BetrayMarker = i.BetrayMarker + 2
                elif choice == 1:
                    i.BetrayMarker = i.BetrayMarker - 2
            if i.BetrayMarker > 100:
                i.BetrayMarker = 100
            elif i.BetrayMarker < 0:
                i.BetrayMarker = 0        
AI1 = AI('AI1')          
AI2 = AI("AI2")
AI3 = AI("AI3")          
AI4 = AI('AI4')
AI5 = AI('AI5')          
AI6 = AI('AI6')
AI7 = AI('AI7')          
AI8 = AI('AI8')
AI9 = AI('AI9')
AI10 = AI('AI10')
AI11 = AI('AI11')          
AI12 = AI("AI12")
AI13 = AI("AI13")          
AI14 = AI('AI14')
AI15 = AI('AI15')          
AI16 = AI('AI16')
AI17 = AI('AI17')          
AI18 = AI('AI18')
AI19 = AI('AI19')
AI20 = AI('AI20')
class AIC:
    BetrayMarker = 50
    games = 0
    Wins = 0
    links = []
    control = True
    def __init__(self, name):
        self.name = name
    def update(self, bru, brubru, brubrubru):
        self.games += 1

    def cws(self, years):
        if years < 2:
            self.Wins += 1
        else:
            self.Wins =- 1
AIC1 = AIC('C1')
AIC2 = AIC("C2")
