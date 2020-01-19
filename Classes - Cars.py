class Cars:
    speed = 0
    wheels = 4
    driverSide = "right-side"
    doors = 5

    def horn(self):
        return "HONK HONK"

    def accelerate(self, amount):
        if amount >= 0:
            self.speed += amount
        return self.speed

    def decelerate(self, amount):
        if amount > self.speed:
            self.speed = 0
        else:
            self.speed -= amount
        return self.speed

    def brakepedal(self):
        if self.speed > 0:
            self.speed = 0
        return self.speed


Mercedes = Cars()
print(type(Mercedes))
print(Mercedes.wheels)
Mercedes.accelerate(1)
print(Mercedes.speed)
Mercedes.accelerate((29))
print(Mercedes.speed)

print(Mercedes.horn())  # functions need ()
Mercedes.brakepedal()
print(Mercedes.speed)


