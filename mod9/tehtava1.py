class Auto:
    def __init__(init, rekisteritunnus, huippunopeus):
        init.rekisteritunnus = rekisteritunnus
        init.huippunopeus = huippunopeus
        init.nopeus = 0
        init.matka = 0
    

auto = Auto("ABC-123", 142)
print(auto.rekisteritunnus)
print(auto.huippunopeus)
print(auto.nopeus)
print(auto.matka)