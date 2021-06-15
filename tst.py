from PyQt5 import *

class CentralWidget(QtGui.QFrame):

    def __init__(self, *args):
        super(CentralWidget, self).__init__(*args)
        self.setStyleSheet("background-color: rgb(255,0,0); margin:5px; border:1px solid rgb(0, 255, 0); ")

if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    mw = QtGui.QMainWindow()
    w = CentralWidget(mw)
    mw.setCentralWidget(w)
    mw.show()
    w.show()
    app.exec_()