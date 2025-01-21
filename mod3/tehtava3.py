sukupuoli = input("mies / nainen: ")
hemoglobiiniarvo = float(input("hemoglobiiniarvo: "))

if (sukupuoli == "mies"):
    if (hemoglobiiniarvo < 134):
        print("Alhainen")
    elif (hemoglobiiniarvo <= 195):
        print("Normaali")
    else:
        print("Korkea")

elif (sukupuoli == "nainen"):
    if (hemoglobiiniarvo < 117):
        print("Alhainen")
    elif (hemoglobiiniarvo <= 175):
        print("Normaali")
    else:
        print("Korkea")

else:
    print("Virheellinen sukupuoli")