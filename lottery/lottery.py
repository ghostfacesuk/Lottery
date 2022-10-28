import random

numlist = []
luckynum = []

mainball = 5
luckyball = 2
retry = 0

while mainball >= 1:
    randball = random.randint(1, 50)
    if randball in numlist:
        retry += 0
    #    print("match, guessing again")
    else:
        numlist.append(randball)
        mainball -= 1

while luckyball >= 1:
    randball = random.randint(1, 12)
    if randball in luckynum:
        retry += 0
   #     print("match, guessing again")
    else:
        luckynum.append(randball)
        luckyball -= 1


print("Lucky numbers:", *numlist)
print("Lucky stars:", *luckynum)
print("\n")