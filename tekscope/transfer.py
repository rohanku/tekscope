"""
Wrapper functions for transferring data to/from the oscilloscope.
"""

import socket
from .raw import (
    send_command,
    query_binary,
    data_source_cmd,
    data_start_cmd,
    data_stop_cmd,
    data_width_cmd,
    data_encdg_cmd,
    curve_cmd,
    DataEncdg,
    AnalogSource,
    DigitalSource,
)
from .parse import parse_ribinary_seq
from .horizontal import record_length

def set_data_source(soc: socket.socket, source: str):
    """
    Specifies source waveform to be transferred from the oscilloscope.
    """
    send_command(soc, data_source_cmd(source))

def set_data_start(soc: socket.socket, start: int):
    """
    Specifies starting data point for waveform transfer.
    """
    send_command(soc, data_start_cmd(start))

def set_data_stop(soc: socket.socket, stop: int):
    """
    Specifies final data point for waveform transfer.
    """
    send_command(soc, data_stop_cmd(stop))

def set_data_width(soc: socket.socket, width: int):
    """
    Specifies data width for waveform transfer.
    """
    send_command(soc, data_width_cmd(width))

def set_data_encdg(soc: socket.socket, encdg: str):
    """
    Specifies data encoding format for waveform transfer.
    """
    send_command(soc, data_encdg_cmd(encdg))

def get_curve(soc: socket.socket) -> bytes:
    """
    Retrieves a curve from the oscilloscope following existing data setting.
    """
    send_command(soc, curve_cmd())
    return query_binary(soc)

def retrieve_waveform(soc: socket.socket, source: str) -> [int]:
    """
    Retrieves a waveform from the oscilloscope as a Python list.
    """
    assert AnalogSource.is_valid(source) or DigitalSource.is_valid(source)
    samples = record_length(soc)
    set_data_start(soc, 1)
    set_data_stop(soc, samples)
    set_data_width(soc, 1)
    set_data_encdg(soc, DataEncdg.BINARY)
    set_data_source(soc, source)
    return parse_ribinary_seq(get_curve(soc), 1)

def retrieve_all_waveforms(soc: socket.socket) -> dict[str, [int]]:
    """
    Retrieves all analog and digital waveforms from the oscilloscope as a dictionary of Python lists.
    """
    samples = record_length(soc)
    set_data_start(soc, 1)
    set_data_stop(soc, samples)
    set_data_width(soc, 1)
    set_data_encdg(soc, DataEncdg.BINARY)

    res = {}
    for source in AnalogSource.SOURCES:
        set_data_source(soc, source)
        res[source] = parse_ribinary_seq(get_curve(soc), 1)
    for source in DigitalSource.SOURCES:
        set_data_source(soc, source)
        res[source] = parse_ribinary_seq(get_curve(soc), 1)

    return res
