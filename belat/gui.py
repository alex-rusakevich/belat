import os
import sys

from PyQt6 import QtGui, QtWidgets, uic
from PyQt6.QtWidgets import QFileDialog

import belat


class MainWindow(QtWidgets.QMainWindow):
    # region Events
    def event_clean_all_input(self):
        self.fromPlainTextEdit.setPlainText("")
        self.toPlainTextEdit.setPlainText("")
        self.fileFromLineEdit.setText("")
        self.fileToLineEdit.setText("")

    def event_open_file_from(self):
        dialog = QFileDialog(self)
        filename = QFileDialog.getOpenFileName(
            dialog,
            "Абярыце файл...",
            filter="Усе падтрымліваемыя файлы (*.txt *.epub *.fb2)",
        )[0]

        if filename != "":
            self.fileFromLineEdit.setText(filename)

    def event_open_file_to(self):
        dialog = QFileDialog(self)
        filename = QFileDialog.getOpenFileName(
            dialog,
            "Абярыце файл...",
            filter="Усе падтрымліваемыя файлы (*.txt *.epub *.fb2)",
        )[0]

        if filename != "":
            self.fileToLineEdit.setText(filename)

    # endregion

    def connectEvents(self):
        self.cleanPushButton.clicked.connect(self.event_clean_all_input)
        self.openFileFromPushButton.clicked.connect(self.event_open_file_from)
        self.openFileToPushButton.clicked.connect(self.event_open_file_to)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi(os.path.join("ui", "belat.ui"), self)

        self.setContentsMargins(11, 11, 11, 11)
        self.setWindowIcon(QtGui.QIcon(os.path.join("ui", "icon.png")))
        self.setWindowTitle(f"belat v{belat.__version__}")

        self.connectEvents()


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()


def run_ui():
    window.show()
    app.exec()
