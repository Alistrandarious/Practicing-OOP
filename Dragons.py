class Dragons:
    def __init__(self, name, kill_count, element, dragongender):
        self.name = name
        self.kill_count = kill_count
        self.element = element
        self.__dragon_gender = dragongender
        self.dragonroar()
        self.animal_kind = "Dragon"
        self.teeth = 100
        self.wings = True
        self.is_good = False
        self.hostile = True

    def greetings(self):
        return self.name + " has killed " + str(self.kill_count) + " living things with " + self.element + "!"

    def dragonroar(self):
        print(f"[DRAGON ROAR] [{self.name} is now created.]")

    def set_gender(self, gre):
        self.__dragon_gender = gre

    def get_gender(self):
        return self.__dragon_gender


if __name__ == "__man__":

    toothless = Dragons("Toothless", 0, "Fire", "male")
    smaug = Dragons("Smaug", 999, "Fire and eating", "male")
    # Lower case object upper class dragon

    print(toothless.greetings())
    print(smaug.greetings())
    print(smaug.name + " has " + str(smaug.teeth) + " teeth ")
    print(smaug.get_gender())
    smaug.set_gender("Still male")
    print(smaug.get_gender())

    ali = Dragons("Ali", 0, "Water", "male")
    print(ali.greetings())

    ali.set_gender("Still male")
    print(ali.get_gender())



