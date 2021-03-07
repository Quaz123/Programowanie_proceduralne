# właściwości - atrybut tworzony dynamicznie

import datetime
class Person:
    """Klasa reprezentująca osobę"""
    def __init__(self, name, birthday):
        self._name = name
        self._birthday = birthday

    @property
    def age(self):
        today = datetime.date.today()
        return today.year - self._birthday.year

    @property
    def name(self):
        return self._name

if __name__ == '__main__':
    john = Person("John", datetime.date(1989,10,3))
    print(john.name)
    print(john.age)