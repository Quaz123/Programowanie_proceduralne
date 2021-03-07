# definicja klasy
class Pet:
    "Klasa reprezentująca domowego zwierzaka"
    def __init__(self, name):  # konstruktor
        self.name = name
        print("Urodził się nowy zwierzak!")
    def talk(self):
        print(f"Cześć. Jestem {self.name}!")
    def __str__(self):
       return f"Obiekt klasy Pet\nimię: {self.name}"



# część główna programu
if __name__ == '__main__':
    my_pet1 = Pet("Topik")  # konkretyzacja obiektu
    my_pet1.talk()          # wywołanie metody instancyjnej
    my_pet2 = Pet("Topcia") # konkretyzacja obiektu
    my_pet2.talk()          # wywołanie metody instancyjnej
    # bezpośredni dostęp do atrybutu name obiektu my_pet1 i mu_pet2
    print(my_pet1.name)
    print(my_pet2.name)
    # wyświetlenie obiektu - pośrednie wywołanie metody __str__ przez print
    print(my_pet2)
