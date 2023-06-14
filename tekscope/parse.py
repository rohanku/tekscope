"""
Utilities for parsing raw bytes received from the oscilloscope.
"""

from .waveform import WaveformMetadata


def parse_ribinary_seq(data: bytes, bytes_nr: int) -> [int]:
    """
    Parses an RI binary received from the oscilloscope to a Python list.
    RI binary is a signed integer binary format with the most significant byte sent first.

    >>> parse_ribinary_seq(bytes([0x7, 0x5, 0xf8, 0xc1]), 2)
    [1797, -1855]
    """
    return [
        int.from_bytes(data[i : i + bytes_nr], "big", signed=True)
        for i in range(0, len(data), bytes_nr)
    ]


def parse_ascii_seq(data: bytes) -> [int]:
    """
    Convert a ASCII sequence received from the oscilloscope to a Python list.

    >>> parse_ascii_seq(b"1,2")
    [1, 2]
    """
    return list(map(int, data.split(b",")))


def parse_wfmoutpre(data: bytes) -> WaveformMetadata:
    """
    Parses the output of the WFMOUTPRE? query and stores relevant values 
    in a `WaveformMetadata` object.

    >>> metadata = parse_wfmoutpre(b'1;8;BINARY;RI;MSB;"Ch1, DC coupling, 100.0mV/div, \
    ... 400.0ns/div, 10000 points, Sample mode";10000;Y;LINEAR;"s";400.0000E-12;-20.0000E-6;0;\
    ... "V";4.0000E-3;0.0E+0;0.0E+0;TIME;ANALOG;0.0E+0;0.0E+0;0.0E+0')
    >>> int(metadata.t_incr * 1e12)
    400
    >>> int(metadata.t_zero * 1e6)
    -20
    >>> int(metadata.v_mult * 1e3)
    4
    >>> int(metadata.v_off)
    0
    >>> int(metadata.v_zero)
    0
    """
    data = data.split(b";")
    if len(data) < 17:
        return None
    return WaveformMetadata(
        float(data[10]),
        float(data[11]),
        float(data[14]),
        float(data[15]),
        float(data[16]),
    )
