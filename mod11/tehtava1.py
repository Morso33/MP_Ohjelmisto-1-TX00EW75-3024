class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi
    
    def tulosta_tiedot(self):
        pass

class Kirja(Julkaisu):
    def __init__(self, nimi, kirjailija, sivumaara):
        super().__init__(nimi)
        self.kirjailija = kirjailija
        self.sivumaara = sivumaara
    
    def tulosta_tiedot(self):
        print(f"Kirja: {self.nimi}\nKirjailija: {self.kirjailija}\nSivumäärä: {self.sivumaara}\n")

class Lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja):
        super().__init__(nimi)
        self.paatoimittaja = paatoimittaja
    
    def tulosta_tiedot(self):
        print(f"Lehti: {self.nimi}\nPäätoimittaja: {self.paatoimittaja}\n")

aku_ankka = Lehti("Aku Ankka", "Aki Hyyppä")
hytti_no_6 = Kirja("Hytti n:o 6", "Rosa Liksom", 200)

aku_ankka.tulosta_tiedot()
hytti_no_6.tulosta_tiedot()
