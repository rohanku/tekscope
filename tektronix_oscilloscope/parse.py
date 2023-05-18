"""
Utilities for parsing raw bytes received from the oscilloscope.
"""


def parse_ascii_seq(data: bytes) -> [int]:
    """
    Convert a ASCII sequence received from the oscilloscope to a Python list.

    >>> parse_ascii_seq(b"1,2")
    [1, 2]
    """
    return list(map(int, data.split(b",")))
