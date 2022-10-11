import mysql.connector
import random

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='ohjelmisto1',
    autocommit=True
)

("Hei, tervetuloa pelaamaan lentopeliä.\n"
 "Aloita valitsemalla haluamasi kohdekaupunki.\n"
 "Valinta tehdään numeronäppäimillä.\n\n"
 "Lentoliikenne takkuaa ja joudut tekemään viisi välilaskua matkallasi.\n"
 "Tehtäväsi on valita välilaskukentät niin, että reittisi kohteeseen olisi mahdollisimman suora,\n"
 "jotta hiilijalanjälkesi olisi mahdollisimman pieni.\n\n"
 "Sinulle annetaan järjestyksessä kaksi vaihtoehtoa,\n"
 "joista valitset sen, jonka ajattelet olevan parempi kokonaisreittisi kannalta.\n"
 "Valitse vaihtoehtojen välillä käyttämällä numeroita 1. tai 2.,\n"
 "tai nuolinäppäimien vasemmalla ja oikealla nuolella.\n"
 "Vastaus lukitaan painamalla enter.\n"
 "Huomaathan, ettet voi muuttaa vastausta lukitsemisen jälkeen!\n\n"
 "Lopuksi näät, kuinka pitkä valitsemasta reitistäsi tuli,\n"
 "ja mikä reitti olisi ollut lyhyin mahdollinen.\n"
 "Paina enter aloittaaksesi peli.\n"
 "Onnea matkaan!")


# kohdekentän valinta

def lahtokentta():
    sql = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident = 'EFHK'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos


print(f"Olet helsingin lentokentällä")


def valilaskukentta1():
    sql = "select name from airport where continent = 'EU' and latitude_deg < 60 and latitude_deg > 55 and type = 'large_airport'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    for i in tulos:
        kentat1 = [random.choice(tulos), random.choice(tulos)]
        return kentat1


def valilaskukentta2():
    sql = "select name from airport where continent = 'EU' and latitude_deg < 55 and latitude_deg > 50 and type = 'large_airport'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    for i in tulos:
        kentat2 = [random.choice(tulos), random.choice(tulos)]
        return kentat2


def valilaskukentta3():
    sql = "select name from airport where continent = 'EU' and latitude_deg < 50 and latitude_deg > 45 and type = 'large_airport'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    for i in tulos:
        kentat3 = [random.choice(tulos), random.choice(tulos)]
        return kentat3


def valilaskukentta4():
    sql = "select name from airport where continent = 'EU' and latitude_deg < 45 and latitude_deg > 40 and type = 'large_airport'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    for i in tulos:
        kentat4 = [random.choice(tulos), random.choice(tulos)]
        return kentat4


def valilaskukentta5():
    sql = "select name from airport where continent = 'EU' and latitude_deg < 40 and latitude_deg > 35 and type = 'large_airport'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    for i in tulos:
        kentat5 = [random.choice(tulos), random.choice(tulos)]
        return kentat5


lentokentat = []
optimikentat = []
kayttajan_valinnat = []



lista = valilaskukentta1()
kysymys1 = input(f"Valitse ensimmäinen kenttä: a. {lista[0]}, b. {lista[1]}")
if kysymys1 == "a":
    kayttajan_valinnat.append(lista[0])
else:
     kayttajan_valinnat.append(lista[1])



lista = valilaskukentta2()
kysymys2 = input(f"Valitse toinen kenttä: a. {lista[0]}, b. {lista[1]}")
if kysymys2 == "a":
    kayttajan_valinnat.append(lista[0])
else:
    kayttajan_valinnat.append(lista[1])



lista = valilaskukentta3()
kysymys3 = input(f"Valitse kolmas kenttä: a. {lista[0]}, b. {lista[1]}")
if kysymys3 == "a":
    kayttajan_valinnat.append(lista[0])
else:
    kayttajan_valinnat.append(lista[1])



lista = valilaskukentta4()
kysymys4 = input(f"Valitse neljäs kenttä: a. {lista[0]}, b. {lista[1]}")
if kysymys4 == "a":
    kayttajan_valinnat.append(lista[0])
else:
    kayttajan_valinnat.append(lista[1])



lista = valilaskukentta5()
kysymys5 = input(f"Valitse viides kenttä: a. {lista[0]}, b. {lista[1]}")
if kysymys5 == "a":
    kayttajan_valinnat.append(lista[0])
else:
    kayttajan_valinnat.append(lista[1])


korjatut1 = []
for j in kayttajan_valinnat:
    name = str(j)
    delthese = "[()],.'¨"
    for char in delthese:
        name = name.replace(char, "")
    korjatut1.append(name)
print(korjatut1)




def kokonaismatka(lentokentat):
    return 1000


def optimaalinen_reitti(lahtokentta, loppukentta, vaihtoehdot):
    lyhyinmatka = (1000000, [])
    for a in vaihtoehdot[0]:
        for b in vaihtoehdot[1]:
            for c in vaihtoehdot[2]:
                for d in vaihtoehdot[3]:
                    for e in vaihtoehdot[4]:
                        reitti = [lahtokentta, a, b, c, d, e, loppukentta]
                        matka_km = kokonaismatka(reitti)
                        if matka_km < lyhyinmatka[0]:
                            lyhyinmatka = (matka_km, reitti)
    return lyhyinmatka


def hiilijalanjalki(lentokentat):
    co2 = 250 * kokonaismatka(lentokentat)
    return co2


print(hiilijalanjalki(lentokentat))
