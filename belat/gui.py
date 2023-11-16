import logging
import os
import sys

from PyQt6 import QtGui, QtWidgets, uic
from PyQt6.QtWidgets import QFileDialog, QMessageBox

import belat
from belat import settings
from belat.exceptions import NotDoneYet
from belat.settings import get_scheme_by_name

logger = logging.getLogger(__name__)


class MainWindow(QtWidgets.QMainWindow):
    # region Events
    def on_event_clean_all_input(self):
        self.fromPlainTextEdit.setPlainText("")
        self.toPlainTextEdit.setPlainText("")
        self.fileFromLineEdit.setText("")
        self.fileToLineEdit.setText("")

    def on_event_open_file_from(self):
        dialog = QFileDialog(self)
        filename = QFileDialog.getOpenFileName(
            dialog,
            "Абярыце файл...",
            filter="Усе падтрымліваемыя файлы (*.txt *.epub *.fb2)",
        )[0]

        if filename != "":
            self.fileFromLineEdit.setText(filename)

    def on_event_open_file_to(self):
        dialog = QFileDialog(self)
        filename = QFileDialog.getOpenFileName(
            dialog,
            "Абярыце файл...",
            filter="Усе падтрымліваемыя файлы (*.txt *.epub *.fb2)",
        )[0]

        if filename != "":
            self.fileToLineEdit.setText(filename)

    def on_event_translate(self):
        schemeFrom_title = self.schemeFromComboBox.currentText()
        schemeTo_title = self.schemeToComboBox.currentText()

        err_msg = QMessageBox()
        err_msg.setIcon(QMessageBox.Icon.Critical)
        err_msg.setWindowTitle("Памылка")

        if schemeFrom_title == schemeTo_title:
            err_msg.setText("Напрамкі трансліту не могуць быць аднолькавымі!")
            err_msg.exec()
            return

        if "Кірыліца" not in (schemeFrom_title, schemeTo_title):
            err_msg.setText("Адным з напрамкаў трансліта павінна быць кірыліца!")
            err_msg.exec()
            return

        scheme = None
        direction = ""

        if schemeFrom_title == "Кірыліца":  # ctl
            scheme = get_scheme_by_name(schemeTo_title)
            direction = "cyr-to-lat"
        elif schemeTo_title == "Кірыліца":  # ltc
            scheme = get_scheme_by_name(schemeFrom_title)
            direction = "lat-to-cyr"

        if self.tabWidget.currentIndex() == 0:  # text mode
            logger.debug("text mode")

            if self.fromPlainTextEdit.toPlainText().strip() == "":
                err_msg.setText("Тэкст для трансліту не можа быць пустым!")
                err_msg.exec()
                return

            text_in = self.fromPlainTextEdit.toPlainText()
            result_txt = ""

            try:
                if direction == "lat-to-cyr":
                    result_txt = scheme.lat_to_cyr(text_in)
                elif direction == "cyr-to-lat":
                    result_txt = scheme.cyr_to_lat(text_in)
            except NotDoneYet:
                logger.warning("NotDoneYet exception was risen and intercepted")
                result_txt = "[Гэты напрамак трансліту яшчэ не гатовы, калі ласка, паспрабуйце іншы]"

            self.toPlainTextEdit.setPlainText(result_txt)
        else:  # file mode
            logger.debug("file mode")

    # endregion

    def connectEvents(self):
        self.cleanPushButton.clicked.connect(self.on_event_clean_all_input)
        self.openFileFromPushButton.clicked.connect(self.on_event_open_file_from)
        self.openFileToPushButton.clicked.connect(self.on_event_open_file_to)
        self.translatePushButton.clicked.connect(self.on_event_translate)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi(os.path.join("ui", "belat.ui"), self)

        self.centralWidget.setContentsMargins(11, 11, 11, 11)
        self.setWindowIcon(QtGui.QIcon(os.path.join("ui", "icon.png")))
        self.setWindowTitle(f"belat v{belat.__version__}")

        self.connectEvents()

        # region Populate comboboxes
        self.schemeFromComboBox.addItem("Кірыліца")
        self.schemeToComboBox.addItem("Кірыліца")

        for scheme in settings.SCHEMES.values():
            self.schemeFromComboBox.addItem(scheme.name)
            self.schemeToComboBox.addItem(scheme.name)

        # Set the second one to be official latin
        official_index = self.schemeToComboBox.findText(
            settings.SCHEMES["official"].name
        )
        self.schemeToComboBox.setCurrentIndex(official_index)
        logger.debug(f"Official scheme index is {official_index}")
        # endregion

        self.statusBar.showMessage("Праграма гатова да працы!")


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()


def run_ui():
    window.show()
    app.exec()
