import random
import matplotlib.pyplot as plt

deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
points=0
results=[]
gx=[]
gy=[]
hashtable={}
totalpoints=0
def drawCard():
    return int(random.choice(deck))

def drawDeck():
    return [drawCard(), drawCard()]

def usableAce(hand):  
    return 1 in hand and sum(hand) + 10 <= 21

def sumHand(hand): 
    if usableAce(hand):
        return sum(hand) + 10
    return sum(hand)

def isBust(hand): 
    return sumHand(hand) > 21

def score(hand):  
    return 0 if isBust(hand) else sumHand(hand)

def compareHands(a, b):
    return float(a > b) - float(a < b)
    
def playGame(randomHit):
    playerHand=drawDeck()
    dealerHand=drawDeck()
    if randomHit==1:
        playerHand.append(drawCard())
    if isBust(playerHand):
        return -1,playerHand,randomHit
    while sumHand(dealerHand)<17:
        dealerHand.append(drawCard())
    reward=compareHands(playerHand,dealerHand)
    return reward,playerHand,randomHit

def playGameLearning():
    playerHand=drawDeck()
    dealerHand=drawDeck()
    if tuple([str(playerHand),1])  in hashtable and tuple([str(playerHand),0]) in hashtable:
        hitScore=hashtable[str(playerHand),1]
        noHitScore=hashtable[str(playerHand),0]
        if hitScore > noHitScore:
            playerHand.append(drawCard())
    if isBust(playerHand):
        return -1
    while sumHand(dealerHand)<17:
        dealerHand.append(drawCard())
    reward=compareHands(playerHand,dealerHand)
    return int(reward)

for c in range(100):
    points=0
    for i in range(1000):
        reward,playerHand,randomHit=playGame(random.getrandbits(1))
        results.append([reward,playerHand,randomHit])
        points=points+reward
        playerHand=[playerHand[0],playerHand[1]]
        if tuple([str(playerHand),randomHit]) in hashtable:
            x= hashtable[str(playerHand),randomHit]
            x=x+reward
            hashtable[str(playerHand),randomHit]=x
        else:
            hashtable[str(playerHand),randomHit]=reward
    
    gx.append([c])
    gy.append(points)
plt.plot(gx, gy)
plt.ylabel("Points")
plt.xlabel("Games Played (1000x)")
plt.title("Black Jack - Random Chance")
plt.show()
gy=[]



def playGamePresetHand(randomHit,playerHand):
    dealerHand=drawDeck()
    if randomHit==1:
        playerHand.append(drawCard())
    if isBust(playerHand):
        return -1,playerHand,randomHit
    while sumHand(dealerHand)<17:
        dealerHand.append(drawCard())
    reward=compareHands(playerHand,dealerHand)
    return reward,playerHand,randomHit
for t in range(1000):
    for c in deck:
        for e in deck:
            playerHand=[c,e]
            reward,playerHand,randomHit=playGamePresetHand(random.getrandbits(1),playerHand)
            results.append([reward,playerHand,randomHit])
            points=points+reward
            playerHand=[playerHand[0],playerHand[1]]
            if tuple([str(playerHand),randomHit]) in hashtable:
                x= hashtable[str(playerHand),randomHit]
                x=x+reward
                hashtable[str(playerHand),randomHit]=x
            else:
                hashtable[str(playerHand),randomHit]=reward

for c in range(100):
    points=0
    for i in range(1000):
        reward=playGameLearning()
        points=points+reward
    gx.append([c])
    gy.append(points)
    totalpoints=totalpoints+points
plt.plot(gx, gy)
plt.ylabel("Points")
plt.xlabel("Games Played (1000x)")
plt.title("Black Jack - Basic Learning (pre-set Hands)")
plt.show()
print(totalpoints/100)