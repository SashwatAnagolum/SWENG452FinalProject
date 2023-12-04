# This Python file uses the following encoding: utf-8

import event_constants

from alarm_clock_state import AlarmClockState


class OffState(AlarmClockState):
    def __init__(self):
        super().__init__()

    def start(self):
        super().clear_screen()

    def exit(self):
        pass

    def next_state(self, event_id):
        if (event_id == event_constants.POWER_EVENT):
            self.exit()
            super().time_state.start()

            return super().time_state
        else:
            return self
