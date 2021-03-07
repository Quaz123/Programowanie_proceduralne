if __name__ == '__main__':
    # zwiększanie licznika referencji
    import sys
    x = [1,2]      # utworzenie obiektu - zwiększenie licznika referencji do obiektu 12
    y = [3,x]      # dodanie do kolekcji - zwiększenie licznika referencji do obiektu 12
    z = x          # zwiększenie licznika referencji do obiektu [1,2]

    print(sys.getrefcount(x))

    # zmniejszanie licznika referencji
    # opuszczenie zasięgu (np. opuszczamy ciało funkcji gdzie zmienna jest zdefiniowana) - zmniejszenie licznika referencji
    def f():
        t = x
        print(sys.getrefcount(x))
    f()
    print(sys.getrefcount(x))
    x = [7]     # nadpisanie zmiennej  - zmniejszenie licznika referencji
    del z       # użycie instrukcji del  - zmniejszenie licznika referencji
    print(sys.getrefcount(y[1]))
    # instrukcjia del nie powoduje usunięcia obiektu!!

    # zależności cykliczne
    p = []
    p.append(p)


