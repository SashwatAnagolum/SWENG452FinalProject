# This Python file uses the following encoding: utf-8
import sys

from PyQt5.QtWidgets import QApplication

from alarm_clock import AlarmClock
from gui_window import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)

    alarm_clock = AlarmClock(MainWindow())
    alarm_clock.initialize()

    sys.exit(app.exec())
