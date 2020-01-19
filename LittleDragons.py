from Dragons import Dragons


class LittleDragons(Dragons):
    def __init__(self):
        super().__init__()
        self.little = "little"
        self.dragonroar()

    def dragonroar(self):
        print("I'm a lil dragon, roar!")


sebastian = LittleDragons("Sebastian", 0, "Fire", "Male")



