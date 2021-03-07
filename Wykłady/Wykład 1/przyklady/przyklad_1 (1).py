if __name__ == '__main__':
    54 # przykład obiektu

    # tożsamość obiektu możemy sprawdzić za pomocą wbudowanej funkcji id
    # w CPytonie będzie to adres w pamięci
    print(id(54))
    print(hex(id(54)))
    print("-"*50)
    # typ obiektu możemy sprawdzić za pomocą funkcji type
    print(type(54))
    print("-"*50)
    # typ int jest przykładem typu niezmiennego w Pythonie
    # i nie posiada żadnego stanu

    # zachowanie obiektu
    for _ in dir(54)[62:]:
        print(_)

    print("-"*50)
    print(int(54).bit_length())
    print(bin(54))
    print(0b110110)
    print("-"*50)
    a = 54
    b = 0b110110
    print(a is b)
    print(a == b)
