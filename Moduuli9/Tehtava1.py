#Kirjoita Auto-luokka, jonka ominaisuuksina ovat rekisteritunnus,
# huippunopeus, tämänhetkinen nopeus ja kuljettu matka.
# Kirjoita luokkaan alustaja, joka asettaa ominaisuuksista
# kaksi ensin mainittua parametreina saatuihin arvoihin.
# Uuden auton nopeus ja kuljetut matka on asetettava automaattisesti nollaksi.
# Kirjoita pääohjelma, jossa luot uuden auton
# (rekisteritunnus ABC-123, huippunopeus 142 km/h).
# Tulosta pääohjelmassa sen jälkeen luodun auton kaikki ominaisuudet.

class Car:
    def __init__(self, regnum, topspeed, curspeed, desttralev):
        self.desttralev = desttralev
        self.curspeed = curspeed
        self.topspeed = topspeed
        self.regnum = regnum

#Pääohjelma

car1 = Car("ABC-123", 142, 0, 0)
print(f"Auton1 rekkari: {car1.regnum} \n"
      f"Auton1 huippunopeus: {car1.topspeed}km/h \n"
      f"Auton1 nopeus: {car1.curspeed} \n"
      f"Auto1 Kulkema matka: {car1.desttralev}")
