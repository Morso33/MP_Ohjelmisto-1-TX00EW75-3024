class Auto:
    def __init__(init, rekisteritunnus, huippunopeus):
        init.rekisteritunnus = rekisteritunnus
        init.huippunopeus = huippunopeus
        init.nopeus = 0
        init.matka = 0

    def kiihdyta(init, nopeus):
        uusi_nopeus = init.nopeus + nopeus
        if (uusi_nopeus > init.huippunopeus):
            uusi_nopeus = init.huippunopeus
        elif (uusi_nopeus < 0):
            uusi_nopeus = 0

        init.nopeus = uusi_nopeus

    

auto = Auto("ABC-123", 142)
auto.kiihdyta(30)
print(auto.nopeus)
auto.kiihdyta(70)
print(auto.nopeus)
auto.kiihdyta(50)
print(auto.nopeus)
auto.kiihdyta(-200)
print(auto.nopeus)