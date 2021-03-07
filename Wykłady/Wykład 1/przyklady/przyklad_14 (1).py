# definicja klasy
class Pet:
    "Klasa reprezentująca domowego zwierzaka"
    counter = 0         # atrybut klasy

    @staticmethod       # dekorator
    def status():       # brak parametru self
        print(f"Ogólna liczba zwierzaków to {Pet.counter}.")
    def __init__(self, name):  # konstruktor
        print("Urodził się nowy zwierzak!")
        self.name = name
        self.__class__.counter += 1         # Pet.counter += 1

    def talk(self):
        print(f"Cześć. Jestem {self.name}!")
    def __str__(self):
       return f"Obiekt klasy Pet\nimię: {self.name}"



# część główna programu
if __name__ == '__main__':
    print(f"\nUzyskanie dostępu do atrybutu klasy Pet.counter: {Pet.counter}\n")

    pet1 = Pet("Topik")
    pet1.talk()
    pet2 = Pet("Topcia")
    pet2.talk()
    pet3 = Pet("Buka")
    pet3.talk()
    Pet.status()        # wywołanie metody klasowej (stytycznej)
    pet1.status()       # wywołanie metody klasowej na instancji klasy
    print(f"\nUzyskanie dostępu do atrybutu klasy poprzez instancję: {pet1.counter}")
