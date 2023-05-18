"""
Wrapper functions for controlling data acquisition.
"""

import socket
from .raw import send_command, query, acquire_numacq_cmd


def num_acq(soc: socket.socket) -> int:
    """
    Retrieves the current number of acquisitions from the oscilloscope.
    """
    send_command(soc, acquire_numacq_cmd())
    int(query(soc))
