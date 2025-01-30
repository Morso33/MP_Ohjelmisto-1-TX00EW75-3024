import random

def random_dice():
    return random.randint(1, 6)

run = True
while (run):
    dice = random_dice()
    print("Dice: ", dice)
    if (dice == 6):
        run = False

print("End")