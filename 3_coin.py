import random


class Coin:
    def __init__(self):
        self.side = 'Tail'

    def throw(self):
        if random.randint(0, 1) == 0:
            self.side = 'Tail'
        else:
            self.side = 'Head'

    def show_side(self):
        return self.side


print("Część I")

toss_1 = Coin()
toss_2 = Coin()
toss_3 = Coin()


def toss_a():
    for i in range(15):
        toss_1.throw()
        print("Toss_1 side: {}".format(toss_1.show_side()))
        toss_2.throw()
        print("Toss_2 side: {}".format(toss_2.show_side()))
        toss_3.throw()
        print("Toss_3 side: {}".format(toss_3.show_side()))


toss_a()

print("Część II")

one = Coin()
two = Coin()
five = Coin()


def game():
    counter = 0
    loses = 0
    win = 0

    for i in range(100):
        while counter < 20:
            one.throw()
            two.throw()
            five.throw()

            if one.show_side() == 'Tail':
                counter += 1
            if two.show_side() == 'Tail':
                counter += 2
            if five.show_side() == 'Tail':
                counter += 5
        if counter == 20:
            win += 1
        elif counter > 20:
            loses += 1

        counter = 0
    print("loses: {}".format(loses))
    print("wins: {}".format(win))


game()
