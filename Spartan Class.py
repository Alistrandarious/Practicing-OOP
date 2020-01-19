class Spartans:
    def __init__(self, name, age, stream, trainer, client):
        self.name = name
        self.age = age
        self.stream = stream
        self.__client = client
        self.__trainer = trainer

    def greetings(self):
        return "Spartan Name: " + self.name + ". Spartan Age: " + str(self.age) + ". Spartan Stream: " + self.stream

    def set_new_client(self, newClient):
        self.__client = newClient

    def get_client(self):
        return {name} + "new client is" + self.__client


ali_shah = Spartans("Ali Shah", 24, "Data", "David", "Deloitte")
print(ali_shah.greetings())
khizer_iqbal = Spartans("Khizer Iqbal", 23, "Data", "David", "The FA")
print(khizer_iqbal.greetings())
khizer_iqbal.set_new_client("Capgemini")
print(khizer_iqbal.greetings())
print(khizer_iqbal.get_client())
harrison_j_obrien= Spartans("Harrison O'Brien", 21, "Data", "David", "The FA")
print(harrison_j_obrien.greetings())
david_harvey = Spartans("David Harvey", 29, "Data", "David", None)
