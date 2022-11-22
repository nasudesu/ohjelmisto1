# Jatka ohjelmaa kirjoittamalla Auto-luokkaan kiihdytä-metodi,
# joka saa parametrinaan nopeuden muutoksen (km/h).
# Jos nopeuden muutos on negatiivinen, auto hidastaa.
# Metodin on muutettava auto-olion nopeus-ominaisuuden arvoa.
# Auton nopeus ei saa kasvaa huippunopeutta suuremmaksi eikä alentua nollaa pienemmäksi.
# Jatka pääohjelmaa siten, että auton nopeutta nostetaan ensin +30 km/h,
# sitten +70 km/h ja lopuksi +50 km/h. Tulosta tämän jälkeen auton nopeus.
# Tee sitten hätäjarrutus määräämällä nopeuden muutos -200 km/h ja tulosta uusi nopeus.
# Kuljettua matkaa ei tarvitse vielä päivittää.

class Car:
    def __init__(self, regnum, topspeed, curspeed, desttralev):
        self.desttralev = desttralev
        self.curspeed = curspeed
        self.topspeed = topspeed
        self.regnum = regnum

    def accel(self, speed):
        self.curspeed += speed
        if self.curspeed > self.topspeed:
            self.curspeed = self.topspeed
        elif self.curspeed < 0:
            self.curspeed = 0

#Pääohjelma

car1 = Car("ABC-123", 142, 0, 0)
print(f"Auton1 rekkari: {car1.regnum} \n"
      f"Auton1 huippunopeus: {car1.topspeed}km/h \n"
      f"Auton1 nopeus: {car1.curspeed} \n"
      f"Auto1 Kulkema matka: {car1.desttralev}")
car1.accel(30)
print(f"Auton1 uusi nopeus: {car1.curspeed}km/h")
car1.accel(70)
print(f"Auton1 uusi nopeus: {car1.curspeed}km/h")
car1.accel(50)
print(f"Auton1 uusi nopeus: {car1.curspeed}km/h")
car1.accel(-200)
print(f"Auton1 uusi nopeus: {car1.curspeed}km/h")