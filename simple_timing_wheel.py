# This Python file uses the following encoding: utf-8

from PySide6.QtCore import QTimer

from timing_wheel import TimingWheel

class SimpleTimingWheel(TimingWheel):
    def __init__(self, num_slots, resolution_in_secs, lock):
        super().__init__(num_slots, resolution_in_secs, lock)
        self.timer = None
        self.initialize_context()

    def start(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.handle_timeout)
        self.timer.start(1000 * self.resolution)

    def handle_timeout(self, child_wheel_values=[]):
        child_wheel_values = []
        self.lock.acquire()

        return super().handle_timeout(child_wheel_values)
