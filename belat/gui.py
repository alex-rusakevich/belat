import logging
import os
import sys
import time

from PyQt6 import QtGui, QtWidgets, uic
from PyQt6.QtWidgets import QFileDialog, QMessageBox

import belat
from belat import settings
from belat.exceptions import NotDoneYet
from belat.settings import RESOURCE_PATH, get_scheme_by_name
from belat.worker import ALLOWED_EXT, Worker

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
        def _on_event_translate(self):
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
                direction = Worker.CTL
            elif schemeTo_title == "Кірыліца":  # ltc
                scheme = get_scheme_by_name(schemeFrom_title)
                direction = Worker.LTC

            if self.tabWidget.currentIndex() == 0:  # text mode
                logger.debug("text mode")

                if self.fromPlainTextEdit.toPlainText().strip() == "":
                    err_msg.setText("Тэкст для трансліту не можа быць пустым!")
                    err_msg.exec()
                    return

                text_in = self.fromPlainTextEdit.toPlainText()
                result_txt = ""

                try:
                    if direction == Worker.LTC:
                        result_txt = scheme.lat_to_cyr(text_in)
                    elif direction == Worker.CTL:
                        result_txt = scheme.cyr_to_lat(text_in)
                except NotDoneYet:
                    logger.warning("NotDoneYet exception was risen and intercepted")
                    result_txt = "[Гэты напрамак трансліту яшчэ не гатовы, калі ласка, паспрабуйце іншы]"

                self.toPlainTextEdit.setPlainText(result_txt)
                return True
            else:  # file mode
                logger.debug("file mode")
                filepath_from = self.fileFromLineEdit.text()
                filepath_to = self.fileToLineEdit.text()

                _, file_from_extension = os.path.splitext(filepath_from)
                _, file_to_extension = os.path.splitext(filepath_to)

                err_msg = QMessageBox()
                err_msg.setIcon(QMessageBox.Icon.Critical)
                err_msg.setWindowTitle("Памылка")

                if file_from_extension != file_to_extension:
                    err_msg.setText("Файлы павінны быць аднаго тыпу!")
                    err_msg.exec()
                    return

                if (file_from_extension not in ALLOWED_EXT) or (
                    file_to_extension not in ALLOWED_EXT
                ):
                    err_msg.setText(
                        f"Тып аднаго з файлаў не падтрымліваецца! Падтрымліваюцца тыпы {', '.join(ALLOWED_EXT)}"
                    )
                    err_msg.exec()
                    return

                enc_from = self.encFromComboBox.currentText()
                enc_to = self.encToComboBox.currentText()
                working_ext = file_from_extension[1:]

                file_worker = Worker(
                    filepath_from,
                    filepath_to,
                    enc_from,
                    enc_to,
                    direction,
                    scheme,
                    working_ext,
                )
                result = file_worker.work()
                self.toPlainTextEdit.setPlainText(result)
                return True

        start_time = time.time()
        fn_res = _on_event_translate(self)
        time_spent = time.time() - start_time

        if fn_res != None:
            self.statusBar.showMessage(f"Гатова! Скончана за {time_spent:.3f} с")
        else:
            self.statusBar.showMessage(
                f"Адбылася памылка, выпраўце яе і паспрабуйце яшчэ раз"
            )

    # endregion

    def connectEvents(self):
        self.cleanPushButton.clicked.connect(self.on_event_clean_all_input)
        self.openFileFromPushButton.clicked.connect(self.on_event_open_file_from)
        self.openFileToPushButton.clicked.connect(self.on_event_open_file_to)
        self.translatePushButton.clicked.connect(self.on_event_translate)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi(os.path.join(RESOURCE_PATH, "ui", "belat.ui"), self)

        self.centralWidget.setContentsMargins(11, 11, 11, 11)
        self.setWindowIcon(QtGui.QIcon(os.path.join(RESOURCE_PATH, "ui", "icon.png")))
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

        # region Populate file encodings
        for enc in ("utf-8", "utf-16", "utf-32", "cp1251", "cp866", "koi8-r"):
            self.encFromComboBox.addItem(enc)
            self.encToComboBox.addItem(enc)
        # endregion

        self.statusBar.showMessage("Праграма гатова да працы!")


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()


def run_ui():
    window.show()
    app.exec()
