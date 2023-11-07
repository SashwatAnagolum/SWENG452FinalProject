# This Python file uses the following encoding: utf-8

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py

from PyQt6.QtWidgets import QApplication, QMainWindow

import event_constants

from ui_form import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.event_handler = None

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.text_boxes = [
            self.ui.text1, self.ui.text2, self.ui.text3,
            self.ui.text4, self.ui.text5, self.ui.text6
        ]

        self.dividers = [
            self.ui.divider1, self.ui.divider2,
            self.ui.divider3, self.ui.divider4
        ]

        self.headings = [self.ui.heading1, self.ui.heading2]

    def get_text_boxes(self):
        return self.text_boxes

    def get_headings(self):
        return self.headings

    def get_dividers(self):
        return self.dividers

    def register_event_handler(self, event_handler):
        self.event_handler = event_handler

    def button1_pressed(self, args):
        self.event_handler.handle_event(event_constants.POWER_EVENT)

    def button2_pressed(self, args):
        self.event_handler.handle_event(event_constants.INPUT_EVENT)

    def button3_pressed(self, args):
        self.event_handler.handle_event(event_constants.MODE_EVENT)
