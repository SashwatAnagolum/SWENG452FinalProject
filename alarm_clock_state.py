# This Python file uses the following encoding: utf-8

import abc
import datetime
import os

from threading import Lock
from just_playback import Playback

from PySide6.QtCore import QThread

from heirarchial_timing_wheel import HeirarchicalTimingWheel
from simple_timing_wheel import SimpleTimingWheel

class AlarmClockState(abc.ABC):
    text_boxes = None
    separators = None
    headings = None

    time_state = None
    temperature_state = None
    alarm_state = None
    off_state = None

    timing_wheels = []
    timer_thread = None
    current_time_values = [0, 0, 0]

    time_values_lock = Lock()
    timing_wheel_lock = Lock()

    @staticmethod
    def initialize_states(time_state_obj, temperature_state_obj,
                          alarm_state_obj, off_state_obj):
        AlarmClockState.time_state = time_state_obj
        AlarmClockState.temperature_state = temperature_state_obj
        AlarmClockState.alarm_state = alarm_state_obj
        AlarmClockState.off_state = off_state_obj

    @staticmethod
    def initialize_timing_wheels():
        AlarmClockState.timing_wheels.append(
            SimpleTimingWheel(
                60, 1, AlarmClockState.timing_wheel_lock
            )
        )

        AlarmClockState.timing_wheels.append(
            HeirarchicalTimingWheel(
                60, AlarmClockState.timing_wheels[-1],
                AlarmClockState.timing_wheel_lock
            )
        )

        AlarmClockState.timing_wheels.append(
            HeirarchicalTimingWheel(
                24, AlarmClockState.timing_wheels[-1],
                AlarmClockState.timing_wheel_lock
            )
        )

        curr_time = datetime.datetime.now()
        AlarmClockState.timing_wheels[2].set_context(
            [curr_time.hour, curr_time.minute, curr_time.second]
        )

        AlarmClockState.timer_thread = QThread()

        for wheel in AlarmClockState.timing_wheels:
            wheel.moveToThread(AlarmClockState.timer_thread)

        AlarmClockState.timer_thread.started.connect(
            AlarmClockState.timing_wheels[0].start
        )

        AlarmClockState.timing_wheels[-1].time_incremented.connect(
            AlarmClockState.update_time_values
        )

        AlarmClockState.timing_wheels[0].timeout_signal.connect(
            AlarmClockState.play_alarm_expiry_tone
        )

        AlarmClockState.timer_thread.start()

    @staticmethod
    def initialize(text_box_refs, heading_box_refs, separator_refs,
                   time_state_obj, temperature_state_obj,
                   alarm_state_obj, off_state_obj
    ):
        AlarmClockState.text_boxes = text_box_refs
        AlarmClockState.headings = heading_box_refs
        AlarmClockState.separators = separator_refs

        AlarmClockState.initialize_states(
            time_state_obj, temperature_state_obj,
            alarm_state_obj, off_state_obj
        )

        AlarmClockState.initialize_timing_wheels()

        return AlarmClockState.off_state

    @staticmethod
    def set_timing_wheel_values(new_time_values):
        with AlarmClockState.timing_wheel_lock:
            for i in range(3):
                AlarmClockState.timing_wheels[i].set_slot_index(
                    new_time_values[2 - i]
                )

            AlarmClockState.update_time_values(
                '.'.join([str(i).zfill(2) for i in new_time_values])
            )

    @staticmethod
    def update_time_values(time_values):
        with AlarmClockState.time_values_lock:
            AlarmClockState.current_time_values = time_values.split('.')

    @staticmethod
    def play_alarm_expiry_tone():
        # pb = Playback(os.path.dirname(__file__) + '/assets/alarm.mp3')
        # pb.play()
        AlarmClockState.alarm_state.notify_alarm_expiry()

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
