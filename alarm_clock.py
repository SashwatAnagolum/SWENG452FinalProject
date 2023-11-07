# This Python file uses the following encoding: utf-8

from alarm_clock_state import AlarmClockState
from time_state import TimeState
from temperature_state import TemperatureState
from alarm_state import AlarmState
from off_state import OffState

class AlarmClock:
    def __init__(self, main_window):
        self.main_window = main_window
        self.current_state = AlarmClockState.initialize(
            main_window.get_text_boxes(),
            main_window.get_headings(),
            main_window.get_dividers(),
            TimeState(), TemperatureState(),
            AlarmState(), OffState()
        )

    def initialize(self):
        self.main_window.register_event_handler(self)
        self.main_window.show()

    def handle_event(self, event_id):
        self.current_state = self.current_state.next_state(event_id)
