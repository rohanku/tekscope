"""
Wrapper functions for controlling horizontal parameters.
"""

import socket
from .raw import send_command, query_ascii, horizontal_recordlength_query


def record_length(soc: socket.socket) -> int:
    """
    Retrieves the horizontal record length from the oscilloscope.
    """
    send_command(soc, horizontal_recordlength_query())
    return int(query_ascii(soc))
