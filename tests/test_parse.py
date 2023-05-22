"""
Tests for data parsing.
"""

import os
import matplotlib.pyplot as plt

from .context import DATA_DIR
from tekscope.parse import parse_ribinary_seq

def test_parse_ribinary_seq():
    """
    Test parsing example RI binary data from a Tektronix 3 MDO oscilloscope.
    """
    with open(os.path.join(DATA_DIR, "ribinary.out"), "rb") as f:
        data = f.read()
        seq = parse_ribinary_seq(data, 1)
        plt.plot(seq)
        plt.show()
