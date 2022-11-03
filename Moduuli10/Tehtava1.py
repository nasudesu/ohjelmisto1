class Elevator:
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.floor = self.alin

    def moveup(self):
        self.floor = self.floor + 1

    def movedown(self):
        self.floor = self.floor - 1

    def moveto(self, num):
        while self.floor != num:
            if self.floor > num:
                elevator1.movedown()
            elif self.floor < num:
                elevator1.moveup()
        print(f"Hissi siirrettykirrokseen: {self.floor}")


elevator1 = Elevator(1, 10)
elevator1.moveto(7)
elevator1.moveto(0)