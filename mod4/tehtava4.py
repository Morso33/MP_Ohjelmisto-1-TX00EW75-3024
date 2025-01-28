import random

random_number = random.randint(1, 10)
while True:
    guess = int(input("Arvaa numbero 1-10: "))
    if guess == random_number:
        print("Oikein!")
        break
    elif guess < random_number:
        print("Korkeampi")
    elif guess > random_number:
        print("Matalampi")