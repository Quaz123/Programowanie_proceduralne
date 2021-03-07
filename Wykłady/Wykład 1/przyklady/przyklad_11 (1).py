# definicja klasy
class Pet:
    """Klasa reprezentująca domowego zwierzaka"""
    def __init__(self, name):  # konstruktor
        self.name = name
        print("Urodził się nowy zwierzak!")



# część główna programu
if __name__ == '__main__':
    my_pet1 = Pet("Topik")   # konkretyzacja obiektu
    my_pet2 = Pet("Topcia")  # konkretyzacja obiektu
    print(my_pet1.name)
    print(my_pet2.name)
    print(my_pet1 is my_pet2)