class Clock:
    hours = 0
    minutes = 0
    seconds = 0

    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    @property
    def hours(self):
        return self._hours

    @hours.setter
    def hours(self, value):
        if 0 <= value < 24:
            self._hours = value
        else:
            raise ValueError("Wartość musi być między 0 a 23!")

    @property
    def minutes(self):
        return self._minutes

    @minutes.setter
    def minutes(self, value):
        if 0 <= value < 60:
            self._minutes = value
        else:
            raise ValueError("Wartość musi być między 0 a 59!")

    @property
    def seconds(self):
        return self._seconds

    @seconds.setter
    def seconds(self, value):
        if 0 <= value < 60:
            self._seconds = value
        else:
            raise ValueError("Wartość musi być między 0 a 59!")

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
        print(f"{self.hours}:{self.minutes}:{self.seconds}")

    def __str__(self):
        return f"Odmierzony czas: {self.hours, self.minutes, self.seconds}"

    def __repr__(self):
        return f"{type(self).__name__}({self.hours!r}, {self.minutes!r}, {self.seconds!r})"


print("\nKlasa Clock:")
a = Clock()
a.display()
a.tick()
a.display()
a.set(22, 59, 59)
a.display()
a.tick()
a.display()
print(str(a))
print(f"Użycie repr() i seed(): {eval(repr(a))}")


class Calendar:
    years = 0
    months = 0
    days = 0

    def __init__(self, years=1900, months=1, days=1):
        self.years = years
        self.months = months
        self.days = days

    @property
    def years(self):
        return self._years

    @years.setter
    def years(self, value):
        if 0 <= value <= 9999:
            self._years = value
        else:
            raise ValueError("Wartość musi być między 0 a 9999!")

    @property
    def months(self):
        return self._months

    @months.setter
    def months(self, value):
        if 1 <= value <= 12:
            self._months = value
        else:
            raise ValueError("Wartość musi być między 1 a 12!")

    @property
    def days(self):
        return self._days

    @days.setter
    def days(self, value):
        if 1 <= value <= 30:
            self._days = value
        else:
            raise ValueError("Wartość musi być między 1 a 30!")

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
print(str(b))
b.passage_of_time()
print(str(b))
b.set(2019, 12, 30)
print(str(b))
b.passage_of_time()
print(str(b))
print(b.is_leap_year())
print(f"Użycie repr() i seed(): {eval(repr(b))}")
