#This is a simulation for p players playing all at the same time.
#Each player has an equal chance to win (uniform)

import random

'''Fixed bet before playing at all'''

#amount of dollars each player has
d = 20
#number of players
p = 10
L = [d]*p
#bet
k = 5

#stores the numer of rounds, the bets, etc.
counts = []
bets = []

num_iterations = 100
#random walk
for i in range(num_iterations):
    L = [d]*p
    #initialize the number of rounds
    count = 0
    while len(L)>1:
        #players put their bet in the pot
        for i in range(len(L)):
            L[i] = L[i] - k
        #one player is randomly chosen to win this round
        index = random.choice(range(len(L)))
        #that player gets the pot
        L[index] = L[index] + k*len(L)
        #zero out this mofo (if someone loses all money)
        while 0 in L:
            del L[L.index(0)]
        #counts the number of rounds
        count = count + 1
    counts.append(count)
print(sum(counts)/len(counts))

##########################################################################

'''Change bet each round (most realistic)'''

#amount of dollars each player has
d = 20
#number of players
p = 10
L = [d]*p
#k = random.choice(range(1,min(L)+1))

#stores the numer of rounds, the bets, etc.
counts = []
bets = []

num_iterations = 10000
#random walk
for i in range(num_iterations):
    L = [d]*p
    #initialize the number of rounds
    count = 0
    while len(L)>1:
        #must bet at least 1 up to player with least amount
        k = random.choice(range(1,min(L)+1))
        bets.append(k)
	#if there are two players left and both of them have an equal amount
        if k == d*p/2:
            print(L)
        #players put their bet in the pot
        for i in range(len(L)):
            L[i] = L[i] - k
        #one player is randomly chosen (uniformly) to win this round
        index = random.choice(range(len(L)))
        #that player gets the pot
        L[index] = L[index] + k*len(L)
        #zero out this mofo (if someone loses all money)
        while 0 in L:
            del L[L.index(0)]
        #counts the number of rounds
        count = count + 1
    counts.append(count)
print(sum(counts)/len(counts))

#if d*p/2, that means someone went all in
max(bets)

#if 1, that means there's a case where that's all someone had left
min(bets)

#average bets
sum(bets)/len(bets)

