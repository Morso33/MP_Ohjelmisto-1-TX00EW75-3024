nimet = []

while True:
    nimi = input("Anna nimi: ")
    if nimi == "":
        break
    if (nimi in nimet):
        print("Aiemmin syötetty nimi")
    else:
        nimet.append(nimi)
        print ("Uusi nimi")

for nimi in nimet:
    print(nimi)
print("End")