class Elevator:
    elevators = 0

    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.floor = self.alin
        Elevator.elevators = Elevator.elevators + 1

    def moveup(self):
        self.floor = self.floor + 1

    def movedown(self):
        self.floor = self.floor - 1

    def moveto(self, num):
        while self.floor != num:
            if self.floor > num:
                Elevator.movedown(self)
            elif self.floor < num:
                Elevator.moveup(self)
        print(f"siirtyy kerrokseen {self.floor}")


class House:
    def __init__(self, alin, ylin, elecount):
        self.alin = alin
        self.ylin = ylin
        self.elecount = elecount
        self.elelist = []

        for i in range(1, elecount + 1):
            self.elelist.append(Elevator(alin, ylin))

    def move_ele(self, elenum, goalfloor):
        elevator = self.elelist[elenum - 1]
        print(f"Hissi {elenum} on kerroksessa {elevator.floor}")
        elevator.moveto(goalfloor)



house = House(1, 10, 3)
house.move_ele(1, 5)
house.move_ele(2, 9)
house.move_ele(1, 8)



