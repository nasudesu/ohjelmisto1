# Tulostaa valikon ja palauttaa käyttäjän valinnan.
def valitse():
    print("1 - syötä uusi")
    print("2 - haku")
    print("0 - lopetus")
    valinta = -1
    while valinta < 0 or valinta > 2:
        valinta = int(input("Valitse: "))
    return valinta

# Lisää uuden lentoaseman annettuun sanakirjaan.
def lisaaUusi():
    icao = input("Aseman ICAO-koodi : ")
    nimi = input("Aseman nimi       : ")
    lentoasemat[icao] = nimi

# Tulostaa halutun aseman annetusta sanakirjasta.
def hae():
    icao = input("Aseman ICAO-koodi : ")
    if icao in lentoasemat:
        print(lentoasemat[icao])
    else:
        print("Tuntematon ICAO-koodi")

#
# Pääohjelma
#
lentoasemat = {}
valinta = valitse()
while valinta != 0:
    if valinta == 1:
        lisaaUusi()
    elif valinta == 2:
        hae()
    valinta = valitse()