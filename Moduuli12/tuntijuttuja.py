import requests

hakusana = input("Anna hakusana tv ohjelmaa: ")
pyynto = "https://api.tvmaze.com/search/shows?q=" + hakusana
try:
    vastaus = requests.get(pyynto)
    if vastaus.status_code==200:
        vastaus_json = vastaus.json()
        for i in vastaus_json:
            print(i["show"]["name"])
except requests.exceptions.RequestException as e:
    print("Hakua ei voitu suorittaa.")

