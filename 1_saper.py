import random


def get_number(a, b, text):
    """F. pobiera l. całk. z zakresu a - b i zwraca tę liczbę"""""
    while True:
        number = int(input(f"{text} (zakres {a} - {b}): "))
        if a <= number <= b:
            return number
        else:
            print("Wyszedłeś poza zakres!")
            continue


def lay_mines(number_of_mines, rows, columns):
    mines = set()
    while len(mines) < number_of_mines:
        m = random.randrange(rows)
        n = random.randrange(columns)
        mines.add((m, n))
    return mines


def number_of_neighbouring_mines(field, mines, rows, columns):
    i = field[0]
    j = field[1]
    count = 0
    for m, n in [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1), (i, j - 1), (i, j + 1), (i + 1, j - 1), (i + 1, j),
                 (i + 1, j + 1), ]:
        if 0 <= m < rows and 0 <= n < columns and (m, n) in mines:
            count += 1
    return count


def create_board(mines, rows, columns, mine="*"):
    board = []
    for i in range(rows):
        line = []
        for j in range(columns):
            if (i, j) in mines:
                line.append(mine)
            else:
                line.append(number_of_neighbouring_mines((i, j), mines, rows, columns))
        board.append(line)
    return board


r = get_number(8, 30, "Podaj liczbę min ")
c = get_number(8, 24, "Podaj liczbę wierszy")
m = get_number(1, r * c - 1, "Podaj liczbę kolumn")
mines = lay_mines(m, r, c)
print(mines)
board = create_board(mines, r, c)

for w in board:
    for el in w:
        print(f"{el:^3}", end="")
    print()
xdxdxdx