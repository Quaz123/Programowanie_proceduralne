from math import sqrt
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import *


class Kalkulator(QWidget):  # dziedziczy właściwości i metody z klasy QWidget
    def __init__(self, parent=None):
        super().__init__(parent)  # zwraca nam klasę rodzica i wywołuje jego konstruktor

        self.interfejs()

    def interfejs(self):  # GUI aplikacji

        etykietaM1 = QLabel("<b>Prosty kalkulator</b>")
        etykietaM1.setFont(QFont('Arial', 13))
        etykietaM1.setAlignment(QtCore.Qt.AlignCenter)
        etykieta1 = QLabel("Liczba 1:", self)
        etykieta2 = QLabel("Liczba 2:", self)
        etykieta3 = QLabel("Wynik:", self)

        # przypisanie widgetów do układu tabelarycznego
        ukladT = QGridLayout()
        ukladT.addWidget(etykietaM1, 0, 1)
        ukladT.addWidget(etykieta1, 1, 0)
        ukladT.addWidget(etykieta2, 1, 1)
        ukladT.addWidget(etykieta3, 1, 2)

        # pola edycyjne
        self.liczba1Edt = QLineEdit()
        self.liczba2Edt = QLineEdit()
        self.wynikEdt = QLineEdit()

        self.wynikEdt.readonly = True  # właściwość obiektu - tylko do odczytu
        self.liczba1Edt.setToolTip('Podaj liczby i wybierz działanie')
        self.liczba2Edt.setToolTip('Podaj liczby i wybierz działanie')

        ukladT.addWidget(self.liczba1Edt, 2, 0)
        ukladT.addWidget(self.liczba2Edt, 2, 1)
        ukladT.addWidget(self.wynikEdt, 2, 2)

        # przyciski
        dodajBtn = QPushButton("Dodaj", self)  # self jest tutaj rodzicem (widgetem nadrzędnym)
        odejmijBtn = QPushButton("Odejmij", self)
        dzielBtn = QPushButton("Mnóż", self)
        mnozBtn = QPushButton("Dziel", self)

        ukladH = QHBoxLayout()
        ukladH.addWidget(dodajBtn)
        ukladH.addWidget(odejmijBtn)
        ukladH.addWidget(dzielBtn)
        ukladH.addWidget(mnozBtn)

        # dodanie instancji ukladH do układuT, wiersz i kolumna, którą chcemy wykorzystać,
        # ilość wierszy i kolumn, które chcemy wykorzystać
        ukladT.addLayout(ukladH, 3, 0, 1, 3)

        dodajBtn.clicked.connect(self.dzialanie)
        odejmijBtn.clicked.connect(self.dzialanie)
        mnozBtn.clicked.connect(self.dzialanie)
        dzielBtn.clicked.connect(self.dzialanie)

        # odstęp
        odstep = QLabel("", self)
        odstep.setFont(QFont('Arial', 13))
        odstep.setAlignment(QtCore.Qt.AlignCenter)
        ukladT.addWidget(odstep, 4, 0)

        # funkcja kwadratowa
        etykietaM2 = QLabel("<b>Kalkulator miejsc zerowych</b>")
        etykietaM2.setFont(QFont('Arial', 13))
        etykietaM2.setAlignment(QtCore.Qt.AlignCenter)
        etykieta4 = QLabel("Podaj A:", self)
        etykieta5 = QLabel("Podaj B:", self)
        etykieta6 = QLabel("Podaj C:", self)
        etykieta7 = QLabel("x1 = ", self)
        etykieta8 = QLabel("x2 = ", self)

        ukladT.addWidget(etykietaM2, 5, 1)
        ukladH1 = QHBoxLayout()
        ukladT.addWidget(etykieta4, 6, 0)
        ukladT.addWidget(etykieta5, 6, 1)
        ukladT.addWidget(etykieta6, 6, 2)

        self.liczbaAEdt = QLineEdit()
        self.liczbaBEdt = QLineEdit()
        self.liczbaCEdt = QLineEdit()
        self.wynikX1Edt = QLineEdit()
        self.wynikX2Edt = QLineEdit()

        self.wynikX1Edt.readonly = True
        self.wynikX2Edt.readonly = True
        self.liczbaAEdt.setToolTip('Wpisz A, B i C a następnie wybierz działanie')
        self.liczbaBEdt.setToolTip('Wpisz A, B i C a następnie wybierz działanie')
        self.liczbaCEdt.setToolTip('Wpisz A, B i C a następnie wybierz działanie')

        ukladT.addWidget(self.liczbaAEdt, 7, 0)
        ukladT.addWidget(self.liczbaBEdt, 7, 1)
        ukladT.addWidget(self.liczbaCEdt, 7, 2)
        ukladH1.addWidget(etykieta7)
        ukladH1.addWidget(self.wynikX1Edt)
        ukladH1.addWidget(etykieta8)
        ukladH1.addWidget(self.wynikX2Edt)
        ukladT.addLayout(ukladH1, 8, 0, 1, 4)

        obliczBtn = QPushButton("Oblicz miejsca zerowe", self)
        obliczBtn.clicked.connect(self.dzialanie2)

        ukladT.addWidget(obliczBtn, 9, 0, 1, 3)

        ukladT.addWidget(odstep, 10, 0)

        # pole
        etykietaM3 = QLabel("<b>Kalkulator pola</b>")
        etykietaM3.setFont(QFont('Arial', 13))
        etykietaM3.setAlignment(QtCore.Qt.AlignCenter)
        etykieta9 = QLabel("Bok 1:", self)
        etykieta10 = QLabel("Bok 2:", self)
        etykieta11 = QLabel("Wysokość:", self)
        etykieta12 = QLabel("Pole (w j^2) =", self)

        ukladT.addWidget(etykietaM3, 11, 1)
        ukladH2 = QHBoxLayout()
        ukladH3 = QHBoxLayout()
        ukladT.addWidget(etykieta9, 12, 0)
        ukladT.addWidget(etykieta10, 12, 1)
        ukladT.addWidget(etykieta11, 12, 2)

        self.liczbaBokaEdt = QLineEdit()
        self.liczbaBokbEdt = QLineEdit()
        self.liczbaWysEdt = QLineEdit()
        self.wynikPoleEdt = QLineEdit()

        self.wynikPoleEdt.readonly = True
        self.liczbaBokaEdt.setToolTip('Wpisz odpowiednie wymiary a następnie wybierz działanie')
        self.liczbaBokbEdt.setToolTip('Wpisz odpowiednie wymiary a następnie wybierz działanie')
        self.liczbaWysEdt.setToolTip('Wpisz odpowiednie wymiary a następnie wybierz działanie')

        ukladT.addWidget(self.liczbaBokaEdt, 13, 0)
        ukladT.addWidget(self.liczbaBokbEdt, 13, 1)
        ukladT.addWidget(self.liczbaWysEdt, 13, 2)
        ukladH2.addWidget(etykieta12)
        ukladH2.addWidget(self.wynikPoleEdt)
        ukladT.addLayout(ukladH2, 14, 0, 1, 3)

        obliczKwadBtn = QPushButton("Oblicz pole kwadratu", self)
        obliczProsBtn = QPushButton("Oblicz pole prostokąta", self)
        obliczTrojBtn = QPushButton("Oblicz pole trójkąta", self)
        obliczTrapBtn = QPushButton("Oblicz pole trapezu", self)
        obliczRownBtn = QPushButton("Oblicz pole równoległoboku", self)
        obliczRombBtn = QPushButton("Oblicz pole rombu", self)
        ukladH3.addWidget(obliczKwadBtn)
        ukladH3.addWidget(obliczProsBtn)
        ukladH3.addWidget(obliczTrojBtn)
        ukladH3.addWidget(obliczTrapBtn)
        ukladH3.addWidget(obliczRownBtn)
        ukladH3.addWidget(obliczRombBtn)
        ukladT.addLayout(ukladH3, 15, 0, 1, 6)
        koniecBtn = QPushButton("Zakończ program", self)
        koniecBtn.resize(koniecBtn.sizeHint())

        ukladT.addWidget(obliczBtn, 15, 0, 1, 3)
        ukladT.addWidget(odstep, 16, 0)
        ukladT.addWidget(koniecBtn, 17, 0, 1, 3)

        # przypisanie utworzonego układu do okna
        self.setLayout(ukladT)

        obliczKwadBtn.clicked.connect(self.dzialanie3)
        obliczProsBtn.clicked.connect(self.dzialanie3)
        obliczTrojBtn.clicked.connect(self.dzialanie3)
        obliczTrapBtn.clicked.connect(self.dzialanie3)
        obliczRownBtn.clicked.connect(self.dzialanie3)
        obliczRombBtn.clicked.connect(self.dzialanie3)
        koniecBtn.clicked.connect(self.koniec)  # naciśnięcie przycisku Koniec wywołuję metodę koniec()

        # self.setGeometry(710, 390, 700, 500)
        self.setWindowIcon(QIcon('icon.jpg'))
        self.setWindowTitle("Kalkulator")
        self.show()

    def koniec(self):
        self.close()

    def closeEvent(self, event):  # przechwytywanie eventu zamykającego program

        odp = QMessageBox.question(
            self, 'Uwaga',
            "Czy na pewno chcesz zakończyć działanie programu?",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if odp == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def dzialanie(self):

        nadawca = self.sender()

        try:
            liczba1 = float(self.liczba1Edt.text())
            liczba2 = float(self.liczba2Edt.text())

            if nadawca.text() == "Dodaj":
                wynik = liczba1 + liczba2
            elif nadawca.text() == "Odejmij":
                wynik = liczba1 - liczba2
            elif nadawca.text() == "Mnóż":
                wynik = liczba1 * liczba2
            else:  # dzielenie
                try:
                    wynik = round(liczba1 / liczba2, 9)
                except ZeroDivisionError:
                    QMessageBox.critical(
                        self, "Błąd", "Nie można dzielić przez zero!")
                    return

            self.wynikEdt.setText(str(wynik))

        except ValueError:
            QMessageBox.warning(self, "Błąd", "Błędne dane", QMessageBox.Ok)

    def dzialanie2(self):
        try:
            a = float(self.liczbaAEdt.text())
            b = float(self.liczbaBEdt.text())
            c = float(self.liczbaCEdt.text())
            delta = (b**2)-(4*a*c)
            if delta > 0:
                x1 = (-b+sqrt(delta))/(2*a)
                x2 = (-b-sqrt(delta))/(2*a)
                self.wynikX1Edt.setText(str(x1))
                self.wynikX2Edt.setText(str(x2))
            elif delta == 0:
                x1 = -b / (2 * a)
                x2 = "Brak"
                self.wynikX1Edt.setText(str(x1))
                self.wynikX2Edt.setText(x2)
            else:
                QMessageBox.information(self, "Informacja", "Brak rozwiązań", QMessageBox.Ok)

        except ValueError:
            QMessageBox.warning(self, "Błąd", "Błędne dane", QMessageBox.Ok)

    def dzialanie3(self):

        nadawca = self.sender()

        try:
            a = float(self.liczbaBokaEdt.text())
            b = float(self.liczbaBokbEdt.text())
            h = float(self.liczbaWysEdt.text())

            if nadawca.text() == "Oblicz pole kwadratu":
                pole = a**2
            elif nadawca.text() == "Oblicz pole prostokąta":
                pole = a*b
            elif nadawca.text() == "Oblicz pole trójkąta":
                pole = a*h/2
            elif nadawca.text() == "Oblicz pole trapezu":
                pole = (a+b)*h*0.5
            else:  # wzór na pole równoległoboku i rombu jest taki sam
                pole = a*h

            self.wynikPoleEdt.setText(str(pole))

        except ValueError:
            QMessageBox.warning(self, "Błąd", "Uzupełnij wszystkie długości", QMessageBox.Ok)


if __name__ == '__main__':  # zapobiega uruchamianiu kodu podczas importowania modułu
    import sys

    app = QApplication(sys.argv)  # tworzymy obiekt aplikacji, która może przyjmować parametry z lini poleceń
    okno = Kalkulator()
    sys.exit(app.exec_())  # uruchomienie głównej pętli programu i rozpoczęcie obsługi zdarzeń
