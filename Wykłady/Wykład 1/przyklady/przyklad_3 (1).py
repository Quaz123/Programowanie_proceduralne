if __name__ == '__main__':
    x = [4]
    y = x
    print("x = ", x)
    print("y = ", y)
    print(x is y)
    print("-"*50)
    # zmiana stanu obiektu (tylko dla obiektów mutowalnych)
    x += [1]
    print("x = ", x)
    print("y = ", y)
    print(x is y)
