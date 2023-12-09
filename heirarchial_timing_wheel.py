# This Python file uses the following encoding: utf-8

from timing_wheel import TimingWheel


class HeirarchicalTimingWheel(TimingWheel):
    def __init__(self, num_slots, child_wheel, lock):
        super().__init__(num_slots, child_wheel.get_range(), lock)

        self.child_wheel = child_wheel
        self.child_wheel.register_parent(self)
        self.register_child(child_wheel)

        self.initialize_context(child_wheel)
