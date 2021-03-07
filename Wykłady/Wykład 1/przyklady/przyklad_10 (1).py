# definicja klasy
class Pet:      #class Pet(object):
    """Klasa reprezentująca domowego zwierzaka"""
    def __init__(self):  # konstruktor
        self.name = "Bobek"
        print("Urodził się nowy zwierzak!")



# część główna programu
if __name__ == '__main__':
    my_pet1 = Pet()  # konkretyzacja obiektu
    my_pet2 = Pet()  # konkretyzacja obiektu
    print(my_pet1.name)
    print(my_pet2.name)
    print(my_pet1 is my_pet2)