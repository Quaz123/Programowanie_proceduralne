from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout, QLineEdit, QPushButton, QHBoxLayout, QMessageBox
from PyQt5.QtCore import Qt


class Kalkulator(QWidget):  # dziedziczy właściwości i metody z klasy QWidget
    def __init__(self, parent=None):
        super().__init__(parent)  # zwraca nam klasę rodzica i wywołuje jego konstruktor

        self.interfejs()

    def interfejs(self):  # GUI aplikacji
        self.resize(500, 300)
        self.setWindowTitle("Prosty kalkulator")
        self.show()

        etykieta1 = QLabel("Liczba 1:", self)
        etykieta2 = QLabel("Liczba 2:", self)
        etykieta3 = QLabel("Wynik:", self)

        # przypisanie widgetów do układu tabelarycznego
        ukladT = QGridLayout()
        ukladT.addWidget(etykieta1, 0, 0)
        ukladT.addWidget(etykieta2, 0, 1)
        ukladT.addWidget(etykieta3, 0, 2)

        # 1-liniowe pola edycyjne
        self.liczba1Edt = QLineEdit()
        self.liczba2Edt = QLineEdit()
        self.wynikEdt = QLineEdit()

        self.wynikEdt.readonly = True   # właściwość obiektu - tylko do odczytu
        self.liczba1Edt.setToolTip('Wpisz <b>liczby</b> i wybierz działanie...')
        self.liczba2Edt.setToolTip('Wpisz <b>liczby</b> i wybierz działanie...')

        ukladT.addWidget(self.liczba1Edt, 1, 0)
        ukladT.addWidget(self.liczba2Edt, 1, 1)
        ukladT.addWidget(self.wynikEdt, 1, 2)

        # przyciski
        dodajBtn = QPushButton("Dodaj", self)   # self jest tutaj rodzicem (widgetem nadrzędnym)
        odejmijBtn = QPushButton("Odejmij", self)
        dzielBtn = QPushButton("Mnóż", self)
        mnozBtn = QPushButton("Dziel", self)
        koniecBtn = QPushButton("Koniec", self)
        koniecBtn.resize(koniecBtn.sizeHint())

        ukladH = QHBoxLayout()
        ukladH.addWidget(dodajBtn)
        ukladH.addWidget(odejmijBtn)
        ukladH.addWidget(dzielBtn)
        ukladH.addWidget(mnozBtn)

        ukladT.addLayout(ukladH, 2, 0, 1, 3)
        ukladT.addWidget(koniecBtn, 3, 0, 1, 3)


        # przypisanie utworzonego układu do okna
        self.setLayout(ukladT)
        koniecBtn.clicked.connect(self.koniec)  # naciśnięcie przycisku Koniec wywołuję metodę koniec()

        self.setGeometry(710, 390, 500, 300)
        self.setWindowIcon(QIcon('icon.jpg'))
        self.setWindowTitle("Prosty kalkulator")
        self.show()

    def koniec(self):
        self.close()

if __name__ == '__main__':  # zapobiega uruchamianiu kodu podczas importowania modułu
    import sys

    app = QApplication(sys.argv)  # tworzymy obiekt aplikacji, która może przyjmować parametry z lini poleceń
    okno = Kalkulator()
    sys.exit(app.exec_())  # uruchomienie głównej pętli programu i rozpoczęcie obsługi zdarzeń
