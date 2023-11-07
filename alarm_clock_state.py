# This Python file uses the following encoding: utf-8
import abc

class AlarmClockState(abc.ABC):
    text_boxes = None
    separators = None
    headings = None

    time_state = None
    temperature_state = None
    alarm_state = None
    off_state = None

    @staticmethod
    def initialize(text_box_refs, heading_box_refs, separator_refs,
        time_state_obj, temperature_state_obj, alarm_state_obj,
        off_state_obj
    ):
        AlarmClockState.text_boxes = text_box_refs
        AlarmClockState.headings = heading_box_refs
        AlarmClockState.separators = separator_refs

        AlarmClockState.time_state = time_state_obj
        AlarmClockState.temperature_state = temperature_state_obj
        AlarmClockState.alarm_state = alarm_state_obj
        AlarmClockState.off_state = off_state_obj

        return AlarmClockState.off_state

    @abc.abstractmethod
    def next_state(self, event_id):
        pass

    @abc.abstractmethod
    def start(self):
        pass

    @abc.abstractmethod
    def exit(self):
        pass

    def clear_screen(self):
        for text_box in AlarmClockState.text_boxes:
            text_box.setText('')

        for heading in AlarmClockState.headings:
            heading.setText('')

        for divider in AlarmClockState.separators:
            divider.setText('')
