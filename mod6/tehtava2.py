import random

def random_dice(max_number):
    return random.randint(1, max_number)

run = True
max_number = int(input("Give a number: "))
while (run):
    dice = random_dice(max_number)
    print("Dice: ", dice)
    if (dice == max_number):
        run = False

print("End")