import random as r 


game = [r.randint(1,6), r.randint(1,6), r.randint(1,6), r.randint(1,6), r.randint(1,6)]

print(game)

def isYam():
  return game.count(1) == 5 or game.count(2) == 5 or game.count(3) == 5 or game.count(4) == 5 or game.count(5) == 5 or game.count(6) == 5
    
print( "is Yam ? {}".format(isYam()) )


def isBrelan():
    return game.count(1) == 3 or game.count(2) == 3 or game.count(3) == 3 or game.count(4) == 3 or game.count(5) == 3 or game.count(6) == 3

print ("is brelan ? {}".format(isBrelan()))

def isCarre():
    return game.count(1) == 4 or game.count(2) == 4 or game.count(3) == 4 or game.count(4) == 4 or game.count(5) == 4 or game.count(6) == 4
     
print("is carré ? {}".format(isCarre()))

def isFull():
    result = {
        1 : game.count(1),
        2 : game.count(2),
        3 : game.count(3),
        4 : game.count(4),
        5 : game.count(5),
        6 : game.count(6)
    }
    return result

print("isFull ? {}".format(isFull()))


count = 0
yam = False
brelan = False
carre = False
full = False

while True:

    game = [r.randint(1,6), r.randint(1,6), r.randint(1,6), r.randint(1,6), r.randint(1,6)]
   
    if isYam() == True:
       yam == True
       print ("yes yam")
       print (game)
       break

while True:
    
    game = [r.randint(1,6), r.randint(1,6), r.randint(1,6), r.randint(1,6), r.randint(1,6)]
   
    if isBrelan() == True:
       brelan == True
       print ("yes brelan")
       print (game)
       break

while True:
    
    game = [r.randint(1,6), r.randint(1,6), r.randint(1,6), r.randint(1,6), r.randint(1,6)]
   
    if isCarre() == True:
       carre == True
       print ("yes carre")
       print (game)
       break


# affiche le résultat de isFull

while True:
    
    game = [r.randint(1,6), r.randint(1,6), r.randint(1,6), r.randint(1,6), r.randint(1,6)]
   
    if isFull() == True:
       full == True
       print ("yes full")
       print (game)
       break
       
    