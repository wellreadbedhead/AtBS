import random

streaksOfSix = 0
coinFlip = []
streak = 0

for experimentNumber in range(100):
    for i in range(100):
        coinFlip.append(random.randint(0,1))
    
    for i in range(len(coinFlip)):
        if coinFlip[i] == coinFlip[i - 1]:
            streak += 1
        else:
            streak = 0
        
        if streak == 6:
            streaksOfSix += 1
            streak = 0

print('Chance of streak: %s%%' % (streaksOfSix / 100))