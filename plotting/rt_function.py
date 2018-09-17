import time
import numpy as np

class RTFunction:
    def __init__(self, expression):
        self.expression = expression

    def set_expression(self, expression):
        try:
            t = time.time()
            test = eval(expression)
            self.expression = expression
        except:
            pass

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

def get_periodicity(timestamps, data):
    """Analysis given data points and returns None if no periodicity is found and the periodicity is it has been detected"""

    total_time = timestamps[-1]-timestamps[0]
    sample_time = total_time/timestamps.size
    fft = np.abs(np.fft.rfft(data - np.mean(data), norm='ortho')) # remove 0 frequency
    # self.plotting_widget.plot(fft)
    # print(sample_time)
    period = 1 / np.fft.fftfreq(fft.size)[np.argmax(fft)] * sample_time * 2

    # check if enough data is collected to assume this period is correct
    if total_time / period > 4.3:
        return period

    return None