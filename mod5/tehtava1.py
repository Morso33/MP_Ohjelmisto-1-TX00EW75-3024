import random

amount = int(input("Montako arpakuutiota? "))

for i in range(amount):
    print("Arvottu luku on", random.randint(1, 6))