"""
Tests for interacting with waveforms in memory.
"""

import numpy as np

from tekscope.waveform import Waveform, WaveformMetadata


def test_waveform():
    """
    Test `Waveform` API.
    """
    metadata = WaveformMetadata(1.6e-9, -504e-6, 20e-3, -125, 0)
    raw_data = [1, 2, 3, 4, 5, 6, 7, 8]
    waveform = Waveform("CH1", metadata, raw_data)

    time = waveform.time()
    voltage = waveform.voltage()

    assert np.all(
        np.isclose(np.array(time), np.array([1.6e-9 * i + -504e-6 for i in range(8)]))
    )
    assert np.all(np.isclose(np.array(voltage), 20e-3 * (np.array(raw_data) + 125)))
