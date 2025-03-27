import requests

API_KEY = "POISTETTU"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def hae_saa(paikkakunta):
    params = {
        "q": paikkakunta,
        "appid": API_KEY,
        "units": "metric", 
        "lang": "fi" 
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        lampotila = data["main"]["temp"]
        kuvaus = data["weather"][0]["description"]
        print(f"Sää paikassa {paikkakunta}: {kuvaus}, {lampotila}°C")
    else:
        print("Virhe: Ei voitu hakea säätietoja")

paikkakunta = input("Anna paikkakunnan nimi: ")
hae_saa(paikkakunta)
