# Deals with positional and keyword parameters

import random

def playGame(player1name, player2name, numberoftimes = 2, numberoffaces = 6):
     ''' This function plays throwing of dice game between two players.
     It takes the names of the two players as keyword parameters and number of times the die
     must be cast as the default parameter '''
     player1score = player2score = 0
     i = 1
     while i <= numberoftimes:
     #for i in range(numberoftimes):
          castnumber = random.randint(1,numberoffaces)
          print('castnumber',castnumber)
          if (i % 2) != 0:
               player1score += castnumber
               print('score1',player1score)
          else:
               player2score += castnumber
               print('score2',player2score)
          i = i + 1
          print('value of i',i)
     if player1score == player2score:
          print('The throwing die game ends in a draw')
     else:
          if player1score > player2score:
               print(player1name + ' has ' + str(player1score) + ' points and has won the game')
          else:
               print(player2name + ' has ' + str(player2score) + ' points and has won the game')

# Calling playGame function
print()
'''
print("Values passed only to mandatory parameters")
playGame('Tom', 'Jerry')
print("-----------------------------------------------------------------------")

print()
print("Values passed to both mandatory and optional parameters")
playGame('Tom', numberoffaces = 8, numberoftimes = 24, player2name = 'Jerry')
print("-----------------------------------------------------------------------")
print()
'''
print("Values passed to mandatory and one optional parameter, order matters when parameter name not used")
playGame('kay kay', 'ma ma ', 5)
print("-----------------------------------------------------------------------")

print()
print("Values passed to mandatory (order matters) and one optional parameter (using the keyword)")
playGame('Tom', 'Jerry', numberoffaces = 8)
   
print("-----------------------------------------------------------------------")
print()
print("The function playGame is called, passing values to mandatory parameters")
playGame('Tom', 'Jerry', numberoffaces = 8, numberoftimes = 24)
print("-----------------------------------------------------------------------")
print()
'''

