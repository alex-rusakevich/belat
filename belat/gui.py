import os
import sys

from PyQt6 import QtGui, QtWidgets, uic


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi(os.path.join("ui", "belat.ui"), self)
        self.setContentsMargins(11, 11, 11, 11)
        self.setWindowIcon(QtGui.QIcon(os.path.join("ui", "icon.png")))


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()


def run_ui():
    window.show()
    app.exec()
