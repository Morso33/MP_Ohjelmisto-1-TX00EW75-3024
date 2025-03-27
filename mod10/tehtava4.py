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
        return f"{self.rekisteritunnus:10} | Huippunopeus: {self.huippunopeus} km/h | Nopeus: {self.nopeus} km/h | Matka: {self.matka:.1f} km"

class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            auto.kiihdyta(random.randint(-10, 15))
            auto.kulje(1)

    def tulosta_tilanne(self):
        print("=" * 50)
        print(f"Kilpailun nimi: {self.nimi}")
        print(f"Kilpailun pituus: {self.pituus} km")
        print("-" * 50)
        for auto in self.autot:
            print(auto)
        print("=" * 50)

    def kilpailu_ohi(self):
        return any(auto.matka >= self.pituus for auto in self.autot)

if __name__ == "__main__":
    autot = [Auto(f"ABC-{i+1}", random.randint(100, 200)) for i in range(10)]
    kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

    tunnit = 0
    while not kilpailu.kilpailu_ohi():
        kilpailu.tunti_kuluu()
        tunnit += 1
        if tunnit % 10 == 0:
            kilpailu.tulosta_tilanne()
    
    print("Lopputilanne:")
    kilpailu.tulosta_tilanne()