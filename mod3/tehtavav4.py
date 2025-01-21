vuosi = int(input("Anna vuosi: "))

if (vuosi % 4 == 0):
    if (vuosi % 100 == 0):
        if (vuosi % 400 == 0):
            print("Karkausvuosi")
        else:
            print("Ei karkausvuosi")
    else:
        print("Karkausvuosi")