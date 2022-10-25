# Nyt ohjelmoidaan autokilpailu. Uuden auton kuljettu matka alustetaan
# automaattisesti nollaksi. Tee pääohjelman alussa lista, joka koostuu
# kymmenestä toistorakenteella luodusta auto-oliosta. Jokaisen auton
# huippunopeus arvotaan 100 km/h ja 200 km/h väliltä. Rekisteritunnus
# luodaan seuraavasti "ABC-1", "ABC-2" jne. Sitten kilpailu alkaa.
# Kilpailun aikana tehdään tunnin välein seuraavat toimenpiteet:
import random


# Jokaisen auton nopeutta muutetaan siten, että nopeuden muutos arvotaan
# väliltä -10 ja +15 km/h väliltä. Tämä tehdään kutsumalla kiihdytä-metodia.

# Kaikkia autoja käsketään liikkumaan yhden tunnin ajan. Tämä tehdään
# kutsumalla kulje-metodia.

# Kilpailu jatkuu, kunnes jokin autoista on edennyt vähintään 10000 kilometriä.
# Lopuksi tulostetaan kunkin auton kaikki ominaisuudet selkeäksi taulukoksi
# muotoiltuna.

class Car:
    created = 0

    def __init__(self, regnum, topspeed, curspeed, desttralev):
        self.desttralev = desttralev
        self.curspeed = curspeed
        self.topspeed = topspeed
        self.regnum = regnum

    def accel(self, speed):
        self.curspeed = self.curspeed + speed
        if self.curspeed > self.topspeed:
            self.curspeed = self.topspeed
        elif self.curspeed < 0:
            self.curspeed = 0

    def travel(self, hour):
        self.desttralev = self.desttralev + (self.curspeed * hour)


# Pääohjelma
cars = []

for i in range(10):
    cars.append(Car(f"ABC-{i + 1}", random.randint(100, 200), 0, 0))

stopper = False
while stopper == False:
    for i in cars:
        i.accel(random.randint(-10, 15))
        i.travel(1)
        if i.desttralev > 10000:
            for n in cars:
                print(n.regnum, n.topspeed, n.curspeed, n.desttralev)
                stopper = True

