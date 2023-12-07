# This Python file uses the following encoding: utf-8

import datetime

from PyQt5.QtCore import QTimer

from time_input_state import TimeInputState

class TimeState(TimeInputState):
    def __init__(self):
        super().__init__('EDIT')

        self.timer = QTimer()
        self.timer.timeout.connect(self.set_time)
    
    def handle_input_event(self):
        super().handle_input_event()

        if self.editing: 
            self.timer.stop()

    def handle_input_select_event(self):
        if self.editing:
            super().handle_input_select_event()
            super().set_timing_wheel_values(self.new_time_values)

            if self.edit_index == 0:
                self.set_time()
                self.timer.start(500)                

    def handle_mode_event(self):
        self.exit()
        super().temperature_state.start()

        return super().temperature_state

    def set_time(self):
        with super().time_values_lock:
            super().text_boxes[0].setText(
                super().current_time_values[0]
            )

            super().text_boxes[1].setText(
                super().current_time_values[1]
            )

            super().text_boxes[2].setText(
                super().current_time_values[2]
            )     

    def start(self):
        super().clear_screen()
        super().headings[0].setText('TIME')
        super().headings[1].setText('VIEW')

        self.set_time()
        self.timer.start(500)

    def exit(self):
        super().exit()
        self.timer.stop()
