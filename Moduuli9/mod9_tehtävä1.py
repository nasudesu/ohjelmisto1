class Car:
    def __init__(self, regnum, topspeed, curspeed, odmeter):
        self.regnum = regnum
        self.topspeed = topspeed
        self.curspeed = curspeed
        self.odmeter = odmeter

car = Car("ABC-123", 142, 0, 0)
print(f"{car.regnum}, {car.topspeed}km/h, {car.regnum}, {car.odmeter}")
