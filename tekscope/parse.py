"""
Utilities for parsing raw bytes received from the oscilloscope.
"""

def parse_ribinary_seq(data: bytes, bytes_nr: int) -> [int]:
    """
    Parses an RI binary received from the oscilloscope to a Python list.
    RI binary is a signed integer binary format with the most significant byte sent first.

    >>> parse_ribinary_seq(bytes([0x7, 0x5, 0xf8, 0xc1]), 2)
    [1797, -1855]
    """
    return [int.from_bytes(data[i:i + bytes_nr], "big", signed=True) for i in range(0, len(data), bytes_nr)]

def parse_ascii_seq(data: bytes) -> [int]:
    """
    Convert a ASCII sequence received from the oscilloscope to a Python list.

    >>> parse_ascii_seq(b"1,2")
    [1, 2]
    """
    return list(map(int, data.split(b",")))
