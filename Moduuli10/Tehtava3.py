class Elevator:
    elevators = 0

    def __init__(self, alin, ylin, elevnum):
        self.elevnum = elevnum
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
        print(f"hissi {self.elevnum} siirtyy kerrokseen {self.floor}")


class House:
    def __init__(self, alin, ylin, elecount):
        self.alin = alin
        self.ylin = ylin
        self.elecount = elecount
        self.elelist = []

        for i in range(1, elecount + 1):
            self.elelist.append(Elevator(alin, ylin, i))

    def move_ele(self, elenum, goalfloor):
        elevator = self.elelist[elenum - 1]
        print(f"Hissi {elenum} on kerroksessa {elevator.floor}")
        elevator.moveto(goalfloor)

    def firealarm(self):
        for i in self.elelist:
            i.moveto(self.alin)



house = House(1, 10, 3)
house.move_ele(1, 5)
house.move_ele(2, 9)
house.move_ele(1, 8)
house.move_ele(1, 7)