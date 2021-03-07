# import modułu
import pickle

# otwieranie pliku w trybie binarnym do odczytu
file = open("data_1.dat", "rb")

# odmarynowywanie obiektów
object_1 = pickle.load(file)
object_2 = pickle.load(file)
object_3 = pickle.load(file)
object_4 = pickle.load(file)
object_5 = pickle.load(file)
# object_6 = pickle.load(file)

# wyświetlanie obiektów
print(object_1)
print(object_2)
print(object_3)
print(object_4)
print(object_5)

# zamknięcie pliku
file.close()


