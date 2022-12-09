import random
import AI_v2
import os
running = True
AIS = [AI_v2.AI1, AI_v2.AI2, AI_v2.AI3, AI_v2.AI4, AI_v2.AI5, AI_v2.AI6, AI_v2.AI7, AI_v2.AI8]
if input("Controls:") == "True":
    AIS.append(AI_v2.AIC1)
    AIS.append(AI_v2.AIC2)
    print("Added Controls")
data = open(input('filename:')+'.csv', 'w')
from threading import Thread
import time


for i in range(1, int(input('# of Runs:'))):
    whatai = random.choice(AIS)
    whatai2 = random.choice(AIS)
    while whatai == whatai2:
        whatai = random.choice(AIS)
        whatai2 = random.choice(AIS)
    player1choice = random.randint(1, 100)
    player2choice = random.randint(1, 100)
    if player1choice >= whatai.BetrayMarker:
        player1choices = 'Betray'
        if player2choice >= whatai2.BetrayMarker:
            player2choices = 'Betray'
            whatai.update(2, 2, whatai2)
            whatai2.update(2, 2, whatai)
            whatai.cws(2)
            whatai2.cws(2)
            player1years = 2
            player2years = 2
        if player2choice < whatai2.BetrayMarker:
            player2choices = 'Silent'
            whatai.update(0, 2, whatai2)
            whatai2.update(3, 1, whatai)
            whatai.cws(0)
            whatai2.cws(3)
            player1years = 0
            player2years = 3
    if player1choice < whatai.BetrayMarker:
        player1choices = 'Silent'

        if player2choice < whatai2.BetrayMarker:
            player2choices = 'Silent'
            whatai.update(1, 1, whatai2)
            whatai2.update(1, 1, whatai)
            whatai.cws(1)
            whatai2.cws(1)
            player1years = 1
            player2years = 1
        
        if player2choice >= whatai2.BetrayMarker:
            player2choices = 'Betray'
            whatai.update(3, 1, whatai2)
            whatai2.update(0, 2, whatai)
            whatai.cws(3)
            whatai2.cws(0)
            player2years = 0
            player1years = 3
    items = [whatai.name, whatai.BetrayMarker, whatai.games, whatai.Wins, player1choices]
    for nme in whatai.links:
        items.append(nme.name)

    items2 = [whatai2.name, whatai2.BetrayMarker, whatai2.games, whatai2.Wins, player2choices]
    for nme in whatai2.links:
        items2.append(nme.name)

    data.write(str(items))
    data.write('\n')
    data.write(str(items2)) 
    data.write('\n')
data.close()
print(' D O N E ')



