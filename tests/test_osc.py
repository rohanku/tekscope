"""
Tests for high-level oscilloscope API.
"""

import matplotlib.pyplot as plt
import pytest
from tekscope import Oscilloscope
from tekscope.raw import AnalogSource


@pytest.mark.skip(reason="testing framework unimplemented")
def test_acquire_analog_sequence():
    """
    Tests acquisition of a length 200 analog sequence.
    """
    osc = Oscilloscope(host="0.0.0.0", port=4000)

    seq = osc.acquire_analog_sequence(200, AnalogSource.CH1)
    plt.plot(seq)
    plt.show()


@pytest.mark.skip(reason="testing framework unimplemented")
def test_retrieve_waveform():
    """
    Tests acquisition of a length 200 analog sequence.
    """
    osc = Oscilloscope(host="0.0.0.0", port=4000)

    seq = osc.retrieve_all_waveforms()
    print(seq.waveform_dict)
