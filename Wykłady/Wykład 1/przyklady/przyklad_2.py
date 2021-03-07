if __name__ == '__main__':
    x = 4
    y = x
    print("x = ", x)
    print("y = ", y)
    print(x is y)
    print("-"*50)
    # zmiana tożsamości obiektu
    x += 1
    print("x = ", x)
    print("y = ", y)
    print(x is y)
