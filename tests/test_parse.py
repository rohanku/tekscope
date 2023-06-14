"""
Tests for data parsing.
"""

import os
import pytest
import matplotlib.pyplot as plt

from tekscope.parse import parse_ribinary_seq
from .context import DATA_DIR


@pytest.mark.skip(reason="currently requires visual inspection")
def test_parse_ribinary_seq():
    """
    Test parsing example RI binary data from a Tektronix 3 MDO oscilloscope.
    """
    with open(os.path.join(DATA_DIR, "ribinary.out"), "rb") as file:
        data = file.read()
        seq = parse_ribinary_seq(data, 1)
        plt.plot(seq)
        plt.show()
