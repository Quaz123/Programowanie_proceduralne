import weakref

a = {11, 22}
a_wref = weakref.ref(a)
if __name__ == '__main__':
    print(a_wref)       # obiekt słabego odwołania
    print(a_wref())
    a = {33, 44}        # niszczymy odwołanie do obiektu {11, 22}
    print(a_wref() is None)
    print('*'*20)
x = {1, 2, 3}
y = x


# dowolna funkcja, która nie jest powiązana z niczonym obiektem
def f():
    print("Żegnaj...")


if __name__ == '__main__':
    end = weakref.finalize(x, f)  # rejetrowanie wywołania zwrotnego na obekcie x (x będzie niszczony)
    print(end.alive)    # wartość True
    del x               # usuwamy referencję do obiektu {1,2,3}
    print(end.alive)    # wartość True
    y = 'Ala'           # usuwamy referencję do obiektu {1,2,3}; następuje wywołanie
                        # funkcji f bo y było ostatnim odwołaniem do obiektu {1,2,3}
    print(end.alive)    # wartość False - nie ma już obiektu {1,2,3}
