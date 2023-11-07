# This Python file uses the following encoding: utf-8

import datetime

from PyQt5 import QtCore

import event_constants

from alarm_clock_state import AlarmClockState

class TimeState(AlarmClockState):
    def __init__(self):
        super().__init__()

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.set_time)

    def next_state(self, event_id):
        if (event_id == event_constants.POWER_EVENT):
            self.exit()
            super().off_state.start()

            return super().off_state
        elif (event_id == event_constants.MODE_EVENT):
            self.exit()
            super().temperature_state.start()

            return super().temperature_state
        else:
            return self


    def set_time(self):
        super().text_boxes[0].setText(
            str(datetime.datetime.now().hour)
        )

        super().text_boxes[1].setText(
            str(datetime.datetime.now().minute)
        )

        super().text_boxes[2].setText(
            str(datetime.datetime.now().second)
        )

    def start(self):
        super().clear_screen()
        super().headings[0].setText('TIME')

        self.set_time()
        self.timer.start(500)

    def exit(self):
        self.timer.stop()
