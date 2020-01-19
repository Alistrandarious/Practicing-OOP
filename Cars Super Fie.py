import time

class Cars:
    speed = 0

    def __init__(self):
        self.__honk()

    def __honk(self):
        print("Honk!")

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

    def emergency_brake(self):
        if self.speed > 0:
            self.speed = 0
            print("Skrzzzzzzzzzzz *clunk*")
        return self.speed

    def set_car_horn(self, horn):
        self.__honk = horn

    def get_car_horn(self):
        return self.__honk()

    def dashboard(self):
        print(f"the car is going at {self.speed} miles per hour.")



class Specs(Cars):
    def __init__(self, make, model):
        super().__init__()
        self.make = make
        self.model = model

    def CarSpecs(self):
        print(f"The make of the car is {self.make}, {self.model}")

    def self_destruct(self):
        print("This car will detonate in 3... ")
        time.sleep(1)
        print("2...")
        time.sleep(1)
        print("1...")
        time.sleep(1)
        print("BOOM!")
        del self


AliG = Specs("Lamborghini", "Aventador")
AliG.accelerate(30)
AliG.dashboard()
AliG.emergency_brake()
AliG.dashboard()
AliG.CarSpecs()
AliG.self_destruct()
AliG.CarSpecs()

# A class that handles the object of the game, and another class that handles the user.