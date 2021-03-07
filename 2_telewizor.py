def get_info(text, a, b):
    while True:
        number = int(input(f"{text} (od {a} do {b}): "))
        if a <= number <= b:
            return number
        else:
            print("Wyszedłeś poza zakres!")
            continue


def switch(z):
    if z == 1:
        tv1.set_channel()
    elif z == 2:
        tv1.set_volume()
    elif z == 3:
        print("Telewizor wyłączony")
        exit()


class Tv:
    channel = 1
    volume = 20

    def set_channel(self):
        self.channel = get_info("Wprowadź numer kanału", 1, 130)

    def set_volume(self):
        self.volume = get_info("Wprowadź poziom głośności", 0, 100)


print("\nWitaj w symulatorze telewizora")
tv1 = Tv()

while True:
    print(f"\nObecnie leci kanał {tv1.channel}. Głośność jest ustwaiona na {tv1.volume}.")
    print("Co chcesz zrobić?")
    print("1. Zmień kanał")
    print("2. Zmień głośność")
    print("3. Wyłącz telewizor")
    x = input()
    switch(int(x))
