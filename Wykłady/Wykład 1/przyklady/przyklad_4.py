if __name__ == '__main__':
    # kopiowanie płytkie

    # kopiowanie dla typów sekwencyjnych
    x = [1,2,3]
    y = x[:]
    print("x = ", x)
    print("y = ", y)
    print("x is y: ", x is y)
    print("-"*50)
    # kopiowanie np. list
    x = [1,2,3]
    y = list(x)
    print("x = ", x)
    print("y = ", y)
    print("x is y: ", x is y)
    print("-"*50)
    # moduł copy
    import copy
    x = [1,2,3]
    y = copy.copy(x)    # działanie uniwersalne
    print("x = ", x)
    print("y = ", y)
    print("x is y: ", x is y)
    print("-"*50)
