numList = []

while (1):
    number = input("Give a number: ")
    if (number == ""):
        break
    numList.append(int(number))

numListSortedReversed = sorted(numList, reverse=True)

for i in numListSortedReversed:
    print(i)
    if (i == 5):
        break

print ("End")