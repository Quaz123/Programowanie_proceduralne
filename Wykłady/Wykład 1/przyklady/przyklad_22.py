# import modułu
import shelve

# tworzenie półki
shelf = shelve.open("data_2.dat")

# zapełnianie półki
shelf["numbers"] = [1, 2, 3, 4]
shelf["letters"] = ["a", "b", "c"]
shelf["x"] = 123.56

# obiekt półki
print("Obiekt półki: ")
print(shelf)

# zapisanie/aktualizacja stanu półki
shelf.sync()

print("Półka: ")
print(list(shelf))
print()
print("Elementy półki: ")
print('x =', shelf["x"])
print('litery =', shelf["letters"])
print('liczby =', shelf["numbers"])

# zamknięcie półki
shelf.close()
print(50*'-')

# otwarcie pliku z półką
shelf = shelve.open("data_2.dat")
for k, v in shelf.items():
    print(k, ' :', v)


# zamknięcie półki
shelf.close()

