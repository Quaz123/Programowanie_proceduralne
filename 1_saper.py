import random


def get_number(a, b, text):
    """F. pobiera l. całk. z zakresu a - b i zwraca tę liczbę"""""
    try:
        while True:
            number = int(input(f"{text} (zakres {a} - {b}): "))
            if a <= number <= b:
                return number
            else:
                print("Wyszedłeś poza zakres!")
                continue
    except ValueError:
        print("Błędna wartość!")


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


def reveal_fields(field, printable_fields, board, rows, columns):
    i = field[0]
    j = field[1]
    if not (0 <= i < rows and 0 <= j < columns) or (i, j) in printable_fields:
        return
    printable_fields.append((i, j))
    if board[i][j] != 0:
        return
    else:
        for m, n in [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1), (i, j - 1), (i, j + 1), (i + 1, j - 1), (i + 1, j),
                     (i + 1, j + 1), ]:
            reveal_fields((m, n), printable_fields, board, rows, columns)


def print_board(board, printable_fields, rows, columns, all_print=False):
    print("    ", end="")
    for n in range(columns):
        print(f"{n:^5}", end="")
    print()
    for i in range(rows):
        print(f"{i:<3}", end="")
        for j in range(columns):
            if (i, j) in printable_fields or all_print:
                print(f"[{board[i][j]:^3}]", end="")
            else:
                print(f"[{' ':3}]", end="")
        print()


def game():
    r = get_number(8, 30, "Podaj liczbę wierszy ")
    c = get_number(8, 24, "Podaj liczbę kolumn")
    m = get_number(1, r * c - 1, "Podaj liczbę min")
    mines = lay_mines(m, r, c)
    board = create_board(mines, r, c)
    printable_fields = []

    while len(printable_fields) < r * c - m:
        print_board(board, printable_fields, r, c, False)
        i = get_number(0, r - 1, "Podaj numer wiersza")
        j = get_number(0, c - 1, "Podaj numer kolumny")
        if (i, j) in mines:
            print("BOOOOOOOOOOOOM !!!!!!!11!1!ONEONE!11ONE")
            print("GAME OVER")
            print_board(board, printable_fields, r, c, True)
            return
        else:
            reveal_fields((i, j), printable_fields, board, r, c)


game()
