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

class Sahkoauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankin_koko):
        super().__init__(rekisteritunnus, huippunopeus)
        self.bensatankin_koko = bensatankin_koko

sahkoauto = Sahkoauto("ABC-15", 180, 52.5)
polttomoottoriauto = Polttomoottoriauto("ACD-123", 165, 32.3)

sahkoauto.kiihdyta(100)
polttomoottoriauto.kiihdyta(120)

sahkoauto.kulje(3)
polttomoottoriauto.kulje(3)

print(f"Sähköauton matkamittarilukema: {sahkoauto.matka} km")
print(f"Polttomoottoriauton matkamittarilukema: {polttomoottoriauto.matka} km")