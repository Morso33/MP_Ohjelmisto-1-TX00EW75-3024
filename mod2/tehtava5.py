leiviskat = float(input("Leiviskät: "))
naulat = float(input("Naulat: "))
luodit = float(input("Luodit: "))

total_weight_leiviskat = ((leiviskat * 20) * 32) * 13.3
total_weight_naulat = (naulat * 32) * 13.3
total_weight_luodit = luodit * 13.3

total_weight_grams = total_weight_leiviskat + total_weight_naulat + total_weight_luodit


total_kg = 0
for n in range(int(total_weight_grams)):
    if (total_weight_grams >= 1000):
        total_kg+=1
        total_weight_grams -=1000

print("Total weight: KG:" + str(total_kg) + " Grams: " + str(round(total_weight_grams)))