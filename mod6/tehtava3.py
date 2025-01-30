def to_liters(gallons):
    return gallons * 3.785

while True:
    gallons = int(input("Give a number: "))
    if gallons < 0:
        break
    print(to_liters(float(gallons)))