def is_prime (n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

while (1):
    number = input("Give a number: ")
    if is_prime(int(number)):
        print("Prime")
    else:
        print("Not prime")