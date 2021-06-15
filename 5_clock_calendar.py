def f(num):
    if len(str(num)) == 1:
        return f"0{num}"
    else:
        return num


class Quantity:
    def __set_name__(self, owner, name):
        self.public_name = name
        self.private_name = '_' + name

    def __get__(self, obj, objtype=None):
        value = getattr(obj, self.private_name)
        return value

    def __set__(self, obj, value):
        if self.public_name == "hours" and 0 <= value < 24:
            setattr(obj, self.private_name, value)
        elif self.public_name == "minutes" and 0 <= value < 60:
            setattr(obj, self.private_name, value)
        elif self.public_name == "seconds" and 0 <= value < 60:
            setattr(obj, self.private_name, value)
        elif self.public_name == "years" and 0 <= value <= 9999:
            setattr(obj, self.private_name, value)
        elif self.public_name == "months" and 1 <= value <= 12:
            setattr(obj, self.private_name, value)
        elif self.public_name == "days" and 1 <= value <= 30:
            setattr(obj, self.private_name, value)
        else:
            raise ValueError("Nieprawidłowa wartość!")


class Clock:
    hours = Quantity()
    minutes = Quantity()
    seconds = Quantity()

    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set(self, v1, v2, v3):
        self.hours, self.minutes, self.seconds = v1, v2, v3

    def tick(self):
        if self.seconds == 59:
            self.seconds = 0
            if self.minutes == 59:
                self.minutes = 0
                if self.hours == 23:
                    self.hours = 0
                else:
                    self.hours += 1
            else:
                self.minutes += 1
        else:
            self.seconds += 1

    def display(self):
        cyfry_dict = {
            '0': ('###', '# #', '# #', '# #', '###'),
            '1': ('  #', '  #', '  #', '  #', '  #'),
            '2': ('###', '  #', '###', '#  ', '###'),
            '3': ('###', '  #', '###', '  #', '###'),
            '4': ('# #', '# #', '###', '  #', '  #'),
            '5': ('###', '#  ', '###', '  #', '###'),
            '6': ('###', '#  ', '###', '# #', '###'),
            '7': ('###', '  #', '  #', '  #', '  #'),
            '8': ('###', '# #', '###', '# #', '###'),
            '9': ('###', '# #', '###', '  #', '###'),
            ':': ('   ', ' # ', '   ', ' # ', '   '),
        }
        number = f"{f(self.hours)}:{f(self.minutes)}:{f(self.seconds)}"
        digits = [cyfry_dict[digit] for digit in str(number)]
        for i in range(5):
            print("  ".join(segment[i] for segment in digits))
        print("\n")

    def __str__(self):
        return f"Odmierzony czas: {self.hours, self.minutes, self.seconds}"

    def __repr__(self):
        return f"{type(self).__name__}({self.hours!r}, {self.minutes!r}, {self.seconds!r})"


print("\nKlasa Clock")
a = Clock()
a.display()
a.tick()
a.display()
a.set(22, 59, 59)
a.display()
a.tick()
a.display()
print(a)
print(f"Użycie repr(): {eval(repr(a))}")


class Calendar:

    def __init__(self, years=1900, months=1, days=1):
        self.years = years
        self.months = months
        self.days = days

    def set(self, v1, v2, v3):
        self.years, self.months, self.days = v1, v2, v3

    def passage_of_time(self):
        if self.days == 30:
            self.days = 1
            if self.months == 12:
                self.months = 1
                if self.years == 9999:
                    self.years = 0
                else:
                    self.years += 1
            else:
                self.months += 1
        else:
            self.days += 1

    def is_leap_year(self):
        return f"Czy rok jest przestępny: {self.years % 4 == 0 and (self.years % 100 != 0 or self.years % 400 == 0)}"

    def __str__(self):
        return f"Odmierzony czas: {self.years, self.months, self.days}"

    def __repr__(self):
        return f"{type(self).__name__}({self.years!r}, {self.months!r}, {self.days!r})"


print("\nKlasa Calendar:")
b = Calendar()
print(b)
b.passage_of_time()
print(b)
b.set(2019, 12, 30)
b.passage_of_time()
print(b)
print(b.is_leap_year())
print(f"Użycie repr(): {eval(repr(b))}")
