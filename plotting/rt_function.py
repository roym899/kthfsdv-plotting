import time
import numpy as np

class RTFunction:
    def __init__(self, expression):
        self.expression = expression

    def back_sample(self, seconds, sample_frequency=50):
        """Samples back in time with a given frequency and for a specified duration"""
        current_time = time.time()
        time_stamps = np.linspace(current_time, current_time-seconds, seconds*50)

        # evaluate function for the current time
        t = time_stamps
        data = eval(self.expression)

        # do not return absolute time, but just offset from current time
        return t-current_time, data

    def sample(self):
        """Samples the function for the current time"""
        t = time.time()
        data = eval(self.expression)
        return t, data