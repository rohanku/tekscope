"""
Tests for high-level oscilloscope API.
"""

import matplotlib.pyplot as plt
from tektronix_oscilloscope import Oscilloscope, AnalogSource


def test_acquire_analog_sequence():
    """
    Tests acquisition of a length 200 analog sequence.
    """
    osc = Oscilloscope(host="169.254.8.194", port=4000)

    seq = osc.acquire_analog_sequence(200, AnalogSource.CH1)
    plt.plot(seq)
    plt.show()
