import random

from prettytable import PrettyTable


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

class Race:
    def __init__(self, name, kmdis, carlist):
        self.name = name
        self.kmdis = kmdis
        self.carlist = carlist

    def onehour(self,):
        for i in self.carlist:
            i.accel(random.randint(-10, 15))
            i.travel(1)

    def printlist(self):
        pt = PrettyTable()
        pt.field_names = ["Rekkari", "Huippunopaus", "Nopeus Tällähetkellä", "Kuljettu matka"]
        for i in self.carlist:
            pt.add_row([f"{i.regnum}",f"{i.topspeed}Km/h",f"{i.curspeed}Km/h",f"{i.desttralev}Km"])
        print(pt)

    def over(self):
        for i in self.carlist:
            if i.desttralev >= self.kmdis:
                return True

# Pääohjelma
cars = []
for i in range(10):
    cars.append(Car(f"ABC-{i + 1}", random.randint(100, 200), 0, 0))

race = Race("Romuralli", 8000, cars)

round1 = 1
stopper = False
print("Kierros 1")
while not stopper:
    race.onehour()
    stopper = race.over()
    if round1 % 10 == 0:
        race.printlist()
        print(f"Kierros {round1}")
    round1 += 1
race.printlist()

