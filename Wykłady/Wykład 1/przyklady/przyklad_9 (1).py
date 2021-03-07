# klasa
class Pet:
    """Klasa reprezentująca domowego zwierzaka"""   # dokumentujący ciąg tekstowy
    pass


if __name__ == '__main__':
    # konkretyzacja obiektu klasy Pet
    my_pet = Pet()
    print(type(my_pet))

    # dodanie atrybutu do instancji klasy Pet
    my_pet.name = "Bobek"
    print(my_pet.name)
