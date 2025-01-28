luvut = []

while True:
    luku = input("Anna luku: ")
    if luku == "":
        break
    luvut.append(float(luku))

luvut.sort()
print("matalin: " + str(luvut[0]))
print("korkein: " + str(luvut[len(luvut)-1]))