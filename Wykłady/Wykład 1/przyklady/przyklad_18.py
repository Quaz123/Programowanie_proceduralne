# właściwości - kontrola dostępu do atrybutów

import datetime
class Person:
    """Klasa reprezentująca osobę"""
    def __init__(self, name, birthday, married = False):
        self._name = name
        self._birthday = birthday
        self.married = married      # kontrola już na etapia tworzenia obiektu

    @property
    def married(self):
        return self._married

    @married.setter
    def married(self, value):
        if not isinstance(value, bool):
            print("Błędna wartość! Ustwaiono wartość False.")
            self._married = False
        else:
            self._married = value

    # @married.deleter
    # def married(self):
    #     print("Nie można usunąć atrybutu!")


    @property
    def age(self):
        today = datetime.date.today()
        return today.year - self._birthday.year

    @property
    def name(self):
        return self._name



if __name__ == '__main__':
    john = Person("John", datetime.date(1989,10,3), True)
    print(john.name)
    print(john.age)
    print(f'ma żonę/męża: {"tak" if john.married else "nie"}')
    # john._married = 'kopytko' # w dalszym wypadku możemy coś popsuć
    print(john.married)

    del john.married
