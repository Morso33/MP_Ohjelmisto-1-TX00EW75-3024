import random

ifirstNum = ""
iSecondNum = ""

for i in range(3):
    ifirstNum += str(random.randint(0,9))

for i in range(4):
    iSecondNum += str(random.randint(1,6))

print("First: " + ifirstNum + " Second: " + iSecondNum)