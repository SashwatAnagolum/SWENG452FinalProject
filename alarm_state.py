# This Python file uses the following encoding: utf-8

import heapq
import os

import event_constants

from alarm_clock_state import AlarmClockState
from time_input_state import TimeInputState

class AlarmState(TimeInputState):
    def __init__(self):
        super().__init__('ADD')

        self.alarm_times = []
        # self.alarm_sound = QSoundEffect()
        # self.alarm_sound.setSource(QUrl.fromLocalFile('./assets/alarm.mp3'))
        # self.alarm_sound.setLoopCount(1)

        self.is_active = False

    def start(self):
        super().clear_screen()
        super().headings[0].setText('ALRM')
        super().headings[1].setText('VIEW')
        self.show_alarm()
        self.is_active = True
    
    def handle_input_event(self):
        super().handle_input_event()

    def handle_input_select_event(self):
        if self.editing:
            super().handle_input_select_event()

            if self.edit_index == 0:
                self.add_alarm_to_timing_wheel()
                self.show_alarm()

    def handle_mode_event(self):
        self.is_active = False
        self.exit()
        super().time_state.start()

        return super().time_state

    def get_alarm_time(self, alarm_time_values):
        total_diff = super().timing_wheels[-1].compute_diff(
            alarm_time_values,
            super().timing_wheels[-1].get_context()
        )

        return total_diff[0] * 3600 + total_diff[1] * 60 + total_diff[2]

    def add_alarm_to_timing_wheel(self):
        super().timing_wheels[-1].add_timer(
            self.new_time_values
        )        

        alarm_time = self.get_alarm_time(
            self.new_time_values
        )

        heapq.heappush(
            self.alarm_times,
            (alarm_time, self.new_time_values)
        )

    def show_alarm(self):
        if not len(self.alarm_times):
            super().text_boxes[0].setText('--')
            super().text_boxes[1].setText('--')
            super().text_boxes[2].setText('--')
        else:
            super().text_boxes[0].setText(str(self.alarm_times[0][1][0]).zfill(2))
            super().text_boxes[1].setText(str(self.alarm_times[0][1][1]).zfill(2))
            super().text_boxes[2].setText(str(self.alarm_times[0][1][2]).zfill(2))

    def pop_alarm(self):
        heapq.heappop(self.alarm_times)

        if self.is_active:
            self.show_alarm()

    def notify_alarm_expiry(self):
        # self.alarm_sound.play()

        self.pop_alarm()
