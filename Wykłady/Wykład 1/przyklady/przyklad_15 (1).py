class MyClass:
    def __init__(self):
        self._x = 9
        self.__y = 13
    def print_attributes(self):
        print("_x: ", self._x)
        print("__y: ", self.__y)

    def _private_method(self):
        print("Jestem metodą prywatną - nazwa chronioną!")

    def __private_method(self):
        print("Jestem metodą prywatną - nazwa prywatną!")


if __name__ == '__main__':
    my_class = MyClass()

    my_class.print_attributes()

    my_class._x = 90
    my_class._MyClass__y = 130      # atrybut __y jest maskowany z użyciem pewnej konwencji nazewniczej

    my_class.print_attributes()

    my_class._private_method()
    my_class._MyClass__private_method()