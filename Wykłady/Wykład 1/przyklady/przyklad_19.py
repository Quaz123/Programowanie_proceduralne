# właściwości - kontrola dostępu do atrybutów

import datetime
class Person:
    """Klasa reprezentująca osobę"""
    def __init__(self, name, birthday, married = False):
        self._name = name
        self._birthday = birthday
        self.married = married      # kontrola już na etapia tworzenia obiektu

    def _get_married(self):
        return self._married

    def _set_married(self, value):
        if not isinstance(value, bool):
            print("Błędna wartość!")
        else:
            self._married = value

    def _del_married(self):
        print("Nie można usunąć atrybutu!")

    married = property(_get_married, _set_married, _del_married, "Ciąg dokumentujący!")

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
    john.married = True
    print(john.married)
    john.married = "not"
    del john.married
