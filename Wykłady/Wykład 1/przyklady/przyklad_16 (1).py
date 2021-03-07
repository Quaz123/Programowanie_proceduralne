class Pet:
    def __init__(self, name):
        self.name = name

if __name__ == '__main__':
    topik = Pet("Topik")
    print(topik.name)
    topik.name = "Topcia"
    print(topik.name)

    print("-"*50)
# właściwości - atrybuty tylko do odczytu
class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

if __name__ == '__main__':
    john = Person("John")
    print(john.name)
    #john.name = "Betty"
    john._name = "Betty"
    print(john.name)