import random

def PlayTurnPageGame(player1name,player2name,numberofpages=500,nooftimes=3):
    
    chit_score = 0
    kit_score = 0
    print('This is player1 turn and name is',player1name)
    for i in range(0,nooftimes):
        
        totalPages1 = random.randint(1,numberofpages)
        chit_score = totalPages1 + chit_score
        print("Chit Chit turns to- " + str(totalPages1))
    print("Chit Chit Score is: " + str(chit_score))
    
    print('This is player2 turn and name is',player2name)
    for j in range(0,nooftimes):
        
        totalPages2 = random.randint(1,numberofpages)
        kit_score = totalPages2 + kit_score
        print("Kit Kit turns to- " + str(totalPages2))
    print("Kit Kit score is: " + str(kit_score))

    if(chit_score > kit_score):
        print("Chit Chit won the game...")
    else:
        print("Kit Kit won the game...")
        
print()
print("Values passed to both mandatory and optional parameters")
PlayTurnPageGame('Chit Chit','Kit Kit',numberofpages=700,nooftimes=4)
print("-----------------------------------------------------------------------")
