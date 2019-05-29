#simulation for two players at a time
#Players are chosen with uniform sampling
#Feel free to change parameters p,d,p,etc.

import random

'''fixes the bet for all games'''

#p players
p = 7
#d dollars
d = 77
#fixes the bet for all games
k = 11
Counts = []
num_iterations = 10000
for i in range(num_iterations):
    count = 0
    L = [d]*p
    while len(L)>1:
        #pick two poeple to play from the list
        L2 = [L.pop(random.randrange(len(L))) for _ in range(2)]
        #record where those two people are
        #both players put some money in the pot (bet)
        for i in range(len(L2)):
            L2[i] = L2[i] - k
        #pick a random person to win
        index = random.choice(range(len(L2)))
        #winner collects his earnings
        L2[index] = L2[index] + 2*k
        #put those players back in
        L = L + L2
        #zero out this mofo
        while 0 in L:
            del L[L.index(0)]
        #counts the number of rounds
        count = count + 1
    Counts.append(count)
#prints the average
print(sum(Counts)/len(Counts))

###############################################


import random


'''changes the bet each time (most realistic)'''

#p players
p = 7
#d dollars
d = 7
Counts = []
num_iterations = 100000
for i in range(num_iterations):
    count = 0
    L = [d]*p
    while len(L)>1:
        #pick two poeple to play from the list
        L2 = [L.pop(random.randrange(len(L))) for _ in range(2)]
        #record where those two people are
        k = random.randint(1,min(L2))
        #both players put some money in the pot (bet)
        for i in range(len(L2)):
            L2[i] = L2[i] - k
        #pick a random person to win
        index = random.choice(range(len(L2)))
        #winner collects his earnings
        L2[index] = L2[index] + 2*k
        #put those players back in
        L = L + L2
        #zero out this mofo
        while 0 in L:
            del L[L.index(0)]
        #counts the number of rounds
        count = count + 1
    Counts.append(count)
#prints the average
print(sum(Counts)/len(Counts))


###############################################

import random

#Displays the rounds from a single game (out of the for-loop)

d = 77
p = 7
L = [d]*p
count = 0
Total = []
while len(L)>1:
    #pick two poeple to play from the list
    L2 = [L.pop(random.randrange(len(L))) for _ in range(2)]
    #record where those two people are
    k = random.randint(1,min(L2))
    print(k)
    #both players put some money in the pot (bet)
    for i in range(len(L2)):
        L2[i] = L2[i] - k
    #pick a random person to win
    index = random.choice(range(len(L2)))
    #winner collects his earnings
    L2[index] = L2[index] + 2*k
    #put those players back in
    L = L + L2
    print(L)
    #zero out this mofo
    while 0 in L:
        del L[L.index(0)]
    #counts the number of rounds
    count = count + 1