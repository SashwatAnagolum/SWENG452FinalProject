# This Python file uses the following encoding: utf-8

from threading import Lock

from PyQt5.QtCore import QObject, pyqtSignal

class TimingWheel(QObject):
    time_incremented = pyqtSignal(str)
    timeout_signal = pyqtSignal()

    def __init__(self, num_slots, resolution_in_secs, lock):
        super().__init__()

        self.num_slots = num_slots
        self.resolution = resolution_in_secs
        self.wheel_range = num_slots * resolution_in_secs
        self.slot_index = 0
        self.parent_wheel = None
        self.child_wheel = None
        self.lock = lock
        self.saved_timers = [[] for i in range(self.num_slots)]
        self.context = []

    def initialize_context(self, child_wheel=None):
        if child_wheel is None:
            self.context = [0]
        else:
            self.context = [0] + [i for i in child_wheel.get_context()]

    def get_range(self):
        return self.wheel_range
    
    def register_parent(self, parent_wheel):
        self.parent_wheel = parent_wheel

    def register_child(self, child_wheel):
        self.child_wheel = child_wheel

    def set_slot_index(self, index):
        self.slot_index = index
        self.context[0] = index

    def get_slot_index(self):
        """
        Returns the index of the current slot the timing
        wheel points to.

        Returns:
            (int): the index of the current slot.
        """
        with self.lock:
            curr_index = self.slot_index

        if self.parent is None:
            return [curr_index]
        else:
            return self.parent.get_slot_index() + [curr_index]

    def get_context(self):
        return self.context
    
    def set_context(self, context):
        self.context = [i for i in context]
        
        if self.child_wheel is not None:
            self.child_wheel.set_context(context[1:])

        self.set_slot_index(self.context[0])

    def compute_diff(self, new, old):
        time_diff = [0 for i in range(len(new))]

        for i in range(len(new) - 1, -1, -1):
            time_diff[i] += new[i] - old[i]

            if time_diff[i] < 0:
                if i > 0:
                    time_diff[i] += 60
                    time_diff[i - 1] -= 1
                else:
                    if len(new) == 3:
                        time_diff[i] += 24
                    else:
                        time_diff[i] += 60

        return time_diff

    def add_timer(self, timeout_values):
        time_diff = self.compute_diff(timeout_values, self.context)

        if time_diff[0] > 0:
            self.saved_timers[
                (time_diff[0] + self.context[0]) % self.num_slots
            ].append(
                (time_diff, [i for i in self.context], timeout_values)
            )
        else:
            if self.child_wheel:
                self.child_wheel.add_timer(
                     timeout_values[1:]
                )
            else:
                self.timeout_signal.emit()

    def check_timers(self):
        index = 0

        while index < len(self.saved_timers[self.context[0]]):
            timer = self.saved_timers[self.context[0]][index]
            diff = self.compute_diff(self.context, timer[1])

            if diff[0] >= timer[0][0]:
                self.saved_timers[self.context[0]].pop(index)

                if self.child_wheel:
                    self.child_wheel.add_timer(timer[2][1:])
                else:
                    self.timeout_signal.emit()
            else:
                index += 1

    def handle_timeout(self, child_wheel_values=[]):
        if (
            (not len(child_wheel_values)) or
            (sum(child_wheel_values) == 0)
        ):
            self.slot_index += 1

        if self.slot_index == self.num_slots:
            self.slot_index = 0

        child_wheel_values = [self.slot_index] + child_wheel_values

        self.context = [i for i in child_wheel_values]
        self.check_timers()

        if self.parent_wheel is not None:
            self.parent_wheel.handle_timeout(child_wheel_values)
        else:
            self.lock.release()
            self.time_incremented.emit(
                '.'.join([str(i).zfill(2) for i in child_wheel_values])
            )
