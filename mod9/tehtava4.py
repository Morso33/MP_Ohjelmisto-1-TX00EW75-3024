import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdyta(self, nopeus):
        uusi_nopeus = self.nopeus + nopeus
        if uusi_nopeus > self.huippunopeus:
            uusi_nopeus = self.huippunopeus
        elif uusi_nopeus < 0:
            uusi_nopeus = 0
        self.nopeus = uusi_nopeus

    def kulje(self, tunnit):
        self.matka += self.nopeus * tunnit

    def __str__(self):
        return f"{self.rekisteritunnus} {self.huippunopeus} {self.nopeus} {self.matka:.1f}"


autot = [Auto(f"ABC-{i+1}", random.randint(100, 200)) for i in range(10)]

kilpailu_kaynnissa = True
while kilpailu_kaynnissa:
    for auto in autot:
        auto.kiihdyta(random.randint(-10, 15))
        auto.kulje(1)
        
        if auto.matka >= 10000:
            kilpailu_kaynnissa = False
            break

# Tulostetaan lopputulokset
print("-" * 24)
for auto in autot:
    print(str(auto))
print("-" * 24)