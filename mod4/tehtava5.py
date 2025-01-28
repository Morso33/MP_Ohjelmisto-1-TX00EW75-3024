kayttajatunnus = "python"
salasana = "rules"

failed_attempts = 0
while True:
    input_kayttaja = input("Käyttäjätunnus: ")
    input_salasana = input("Salasana: ")

    if (input_kayttaja == kayttajatunnus and input_salasana == salasana):
        print("Tervetuloa!")
        break
    else:
        failed_attempts += 1
        print("Väärä käyttäjätunnus tai salasana.")

    if (failed_attempts >= 5):
        print("Pääsy evätty")
        break