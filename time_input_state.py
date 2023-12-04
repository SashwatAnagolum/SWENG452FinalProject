# This Python file uses the following encoding: utf-8

from abc import abstractmethod

from PySide6.QtCore import QTimer

import event_constants

from alarm_clock_state import AlarmClockState

class TimeInputState(AlarmClockState):
    def __init__(self, editing_text):
        super().__init__()
        self.editing_timer = QTimer()
        self.editing_timer.timeout.connect(self.set_editable_time)

        self.editing = False
        self.edit_index = 0
        self.new_time_values = [0, 0, 0]
        self.max_values = [24, 60, 60]
        self.is_blinking = False
        self.editing_text = editing_text

    def handle_input_event(self):
        if not self.editing:
            self.editing = True
            self.editing_timer.start(500)

            super().headings[1].setText(self.editing_text)

            self.new_time_values = [0, 0, 0]
            self.set_editable_time()
        else:
            self.new_time_values[self.edit_index] += 1

            self.new_time_values[self.edit_index] = (
                self.new_time_values[self.edit_index] %
                self.max_values[self.edit_index]
            )

    def handle_input_select_event(self):
        if self.editing:
            if self.edit_index == 2:
                self.editing = False
                self.editing_timer.stop()
                super().headings[1].setText('VIEW')             

            self.edit_index = (self.edit_index + 1) % 3

    @abstractmethod
    def handle_mode_event(self):
        pass

    def next_state(self, event_id):
        if event_id == event_constants.POWER_EVENT:
            self.exit()
            super().off_state.start()

            return super().off_state

        if event_id == event_constants.INPUT_EVENT:
            self.handle_input_event()

        if event_id == event_constants.INPUT_SELECT_EVENT:
            self.handle_input_select_event()

        if event_id == event_constants.MODE_EVENT:
            return self.handle_mode_event()

        return self     

    def set_editable_time(self):
        for i in range(3):
            if i != self.edit_index:
                super().text_boxes[i].setText(
                    str(self.new_time_values[i]).zfill(2)
                )
            else:
                if self.is_blinking:
                    super().text_boxes[i].setText(
                        str(self.new_time_values[i]).zfill(2)
                    )
                else:
                    super().text_boxes[i].setText(
                        ''
                    )

                self.is_blinking = not self.is_blinking

    def exit(self):
        self.editing_timer.stop()
        self.editing = False
        self.edit_index = 0
