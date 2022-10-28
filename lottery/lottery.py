import random

num0 = []

mainball = 5
luckyball = 2
mainpos = 0
retry = 0

while mainball >= 1:
    randball = random.randint(1, 50)
    if randball in num0:
        retry += 0
    #    print("match, guessing again")
    else:
        num0.append(randball)
        mainpos += 1
        mainball -= 1

while luckyball >= 1:
    randball = random.randint(1, 12)
    if randball in num0:
        retry += 0
   #     print("match, guessing again")
    else:
        num0.append(randball)
        mainpos += 1
        luckyball -= 1

print("Your lucky numbers are... ")
print(*num0, sep=', ')
print(" \n")