class Car:
    def __init__(self, regnum, topspeed, curspeed=0, desttralev=0):
        self.desttralev = desttralev
        self.curspeed = curspeed
        self.topspeed = topspeed
        self.regnum = regnum

    def travel(self, hour):
        self.desttralev += self.curspeed * hour

    def accel(self, speed):
        self.curspeed = self.curspeed + speed
        if self.curspeed > self.topspeed:
            self.curspeed = self.topspeed
        elif self.curspeed < 0:
            self.curspeed = 0


class Battery_car(Car):
    def __init__(self, regnum, topspeed, battery_capacity):
        super().__init__(regnum, topspeed)
        self.battery_capacity = battery_capacity

    def print_info(self):
        print(f"Sähköauto1\n"
              f"Rekkari: {self.regnum} "
              f"Huippunopeus: {self.topspeed} "
              f"Ajanut: {self.desttralev} km (matkan)")


class Engine_car(Car):
    def __init__(self, regnum, topspeed, gas_tank):
        super().__init__(regnum, topspeed, )
        self.gas_tank = gas_tank

    def print_info(self):
        print(f"Bensaauto1\n"
              f"Rekkari: {self.regnum} "
              f"Huippunopeus: {self.topspeed} "
              f"Ajanut: {self.desttralev} km (matkan)")


batcar1 = Battery_car("ABC-15", 180, 52.5)
engicar1 = Engine_car("ACD-123", 165, 32.3)

batcar1.accel(140)
engicar1.accel(150)

batcar1.travel(3)
engicar1.travel(3)

batcar1.print_info()
engicar1.print_info()
