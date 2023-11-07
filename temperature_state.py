# This Python file uses the following encoding: utf-8

import random

from PyQt6 import QtCore

import event_constants

from alarm_clock_state import AlarmClockState

class TemperatureState(AlarmClockState):
    def __init__(self):
        super().__init__()

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.set_temperature)

        self.stream_mode = False
        self.temp_stream_period = 2500

    def start(self):
        super().clear_screen()
        super().headings[0].setText('TEMP')
        super().separators[0].setText('.')

        self.set_temperature()

    def exit(self):
        self.timer.stop()
        self.stream_mode = False

    def set_temperature(self):
        temp = str(round(random.uniform(0, 100), 5))

        whole, decimal = temp.split('.')
        whole = whole.zfill(2)
        decimal = decimal[:2].ljust(2, '0')

        super().text_boxes[0].setText(whole)
        super().text_boxes[1].setText(decimal[:2])

    def next_state(self, event_id):
        if (event_id == event_constants.INPUT_EVENT):
            if self.stream_mode:
                self.timer.stop()
            else:
                self.timer.start(self.temp_stream_period)

            self.stream_mode = not self.stream_mode
        elif (event_id == event_constants.MODE_EVENT):
            self.exit()
            super().alarm_state.start()

            return super().alarm_state
        elif (event_id == event_constants.POWER_EVENT):
            self.exit()
            super().off_state.start()

            return super().off_state

        return self
