"""
Wrapper functions for transferring data to/from the oscilloscope.
"""

import socket
from .raw import (
    send_command,
    query,
    data_source_cmd,
    data_start_cmd,
    data_stop_cmd,
    data_width_cmd,
    data_encdg_cmd,
    curve_cmd,
    DataEncdg,
)
from .parse import parse_ascii_seq


def retrieve_analog_sequence(soc: socket.socket, source: str) -> [int]:
    """
    Retrieves an analog sequence from the oscilloscope as a Python list.
    """
    send_command(soc, data_source_cmd(source))
    send_command(soc, data_start_cmd(1))
    send_command(soc, data_stop_cmd(1000))
    send_command(soc, data_width_cmd(1))
    send_command(soc, data_encdg_cmd(DataEncdg.ASCII))
    send_command(soc, "*OPC?")
    query(soc)
    send_command(soc, curve_cmd())
    return parse_ascii_seq(query(soc))
