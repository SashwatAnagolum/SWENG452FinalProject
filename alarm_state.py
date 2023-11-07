# This Python file uses the following encoding: utf-8

import event_constants

from alarm_clock_state import AlarmClockState

class AlarmState(AlarmClockState):
    def __init__(self):
        pass

    def start(self):
        super().clear_screen()
        super().headings[0].setText('ALRM')

    def exit(self):
        pass

    def next_state(self, event_id):
        if (event_id == event_constants.INPUT_EVENT):
            pass
        elif (event_id == event_constants.MODE_EVENT):
            self.exit()
            super().time_state.start()

            return super().time_state
        elif (event_id == event_constants.POWER_EVENT):
            self.exit()
            super().off_state.start()

            return super().off_state

        return self
