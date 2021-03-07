if __name__ == '__main__':
    # wady kopiowania płytkiego
    import copy
    x = [1,[2,3]]
    y = copy.copy(x)
    print("x = ", x)
    print("y = ", y)
    print("x is y: ", x is y)
    print("-"*50)
    x = [1,[2,3]]
    y = copy.copy(x)
    y.append(4)         # OK
    print("x = ", x)
    print("y = ", y)
    print("x is y: ", x is y)
    print("-"*50)
    x = [1,[2,3]]
    y = copy.copy(x)
    y[1].append(4)      # problem
    print("x = ", x)
    print("y = ", y)
    print("x is y: ", x is y)
    print("-"*50)
    # rozwiązanie: kopia głęboka (rekurencyjne kopiowanie drzewa obiektu)
    x = [1,[2,3]]
    y = copy.deepcopy(x)
    y[1].append(4)      # problem
    print("x = ", x)
    print("y = ", y)
    print("x is y: ", x is y)

    # kopiowanie głębokie działa nawet przy odwołaniach cyklicznych
    a = [22, 33]
    b = [a, 44]
    print("a = ", a)
    print("b = ", b)
    a.append(b)
    print("a = ", a)
    c = copy.deepcopy(a)
    print("c = ", c)