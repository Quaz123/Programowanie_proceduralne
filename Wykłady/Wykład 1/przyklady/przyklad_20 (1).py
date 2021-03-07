# import modułu
import pickle


# otwieranie pliku w trybie binarnym do odczytu
file = open("data_1.dat", "wb")

# tworzenie obiektów różnych typów

# lista
list_ = ["abc", 1, 12, "XYZ"]
# krotka
tuple_ = ('a', ('b', 'c'), list_)
# liczba zmiennoprzecinkowa
float_ = 4.56
# słownik
dict_ = {"a":1,"b":3,"c":5}
# zbiór
set_ = {3,4,5,5}

# marynowanie
pickle.dump(list_, file)
pickle.dump(tuple_, file)
pickle.dump(float_, file)
pickle.dump(dict_, file)
pickle.dump(set_, file)

# zamykanie pliku
file.close()


