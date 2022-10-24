# Laajenna ohjelmaa siten, että mukana on kulje-metodi, joka saa
# parametrinaan tuntimäärän. Metodi kasvattaa kuljettua matkaa sen
# verran kuin auto on tasaisella vauhdilla annetussa tuntimäärässä edennyt.
# Esimerkki: auto-olion tämänhetkinen kuljettu matka on 2000 km.
# Nopeus on 60 km/h. Metodikutsu auto.kulje(1.5) kasvattaa kuljetun
# matkan lukemaan 2090 km.

class Car:
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


#Pääohjelma

car1 = Car("ABC-123", 142, 0, 0)
print(f"Auton1 rekkari: {car1.regnum} \n"
      f"Auton1 huippunopeus: {car1.topspeed}km/h \n"
      f"Auton1 nopeus: {car1.curspeed} \n"
      f"Auto1 Kulkema matka: {car1.desttralev}")

#Nopeuden testaus#
car1.accel(30)
print(f"Auton1 uusi nopeus: {car1.curspeed}km/h")
car1.accel(70)
print(f"Auton1 uusi nopeus: {car1.curspeed}km/h")
car1.accel(50)
print(f"Auton1 uusi nopeus: {car1.curspeed}km/h")
car1.accel(-200)
print(f"Auton1 uusi nopeus: {car1.curspeed}km/h")
car1.accel(50)
print(f"Auton1 uusi nopeus: {car1.curspeed}km/h")
#Nopeuden testaus#

#Kuljettu matka#
car1.travel(1)
print(f"Auton1 uusi matka: {car1.desttralev}m.")
car1.travel(1)
print(f"Auton1 uusi matka: {car1.desttralev}m.")
car1.travel(1)
print(f"Auton1 uusi matka: {car1.desttralev}m.")
car1.travel(3)
print(f"Auton1 uusi matka: {car1.desttralev}m.")
car1.travel(-6)
print(f"Auton1 uusi matka: {car1.desttralev}m.")
#Kuljettu matka#