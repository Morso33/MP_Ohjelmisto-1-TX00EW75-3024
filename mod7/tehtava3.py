#Kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi. Ohjelma kysyy käyttäjältä, haluaako tämä syöttää uuden lentoaseman, hakea jo syötetyn lentoaseman tiedot vai lopettaa. Jos käyttäjä valitsee uuden lentoaseman syöttämisen, ohjelma kysyy käyttäjältä lentoaseman ICAO-koodin ja nimen. Jos käyttäjä valitsee haun, ohjelma kysyy ICAO-koodin ja tulostaa sitä vastaavan lentoaseman nimen. Jos käyttäjä haluaa lopettaa, ohjelman suoritus päättyy. Käyttäjä saa valita uuden toiminnon miten monta kertaa tahansa aina siihen asti, kunnes hän haluaa lopettaa. (ICAO-koodi on lentoaseman yksilöivä tunniste. Esimerkiksi Helsinki-Vantaan lentoaseman ICAO-koodi on EFHK. Löydät koodeja helposti selaimen avulla.)

airport_codes = []
airport_names = []

def get_airport_by_code(code):
    if code in airport_codes:
        return airport_names[airport_codes.index(code)]
    else:
        return "Not found"
    
def add_airport (code, name):
    airport_codes.append(code)
    airport_names.append(name)
    print ("New airport added")

while True:
    action = input("Add, search, or quit: ")
    if action.lower() == "add":
        code = input("Give ICAO code: ")
        name = input("Give name: ")
        add_airport(code, name)
    elif action.lower() == "search":
        code = input("Give ICAO code: ")
        print (get_airport_by_code(code))
    else:
        break