"""
Tests of API for directly interacting with the oscilloscope's socket server.
"""

import socket
import tektronix_oscilloscope.raw as osc_raw


def test_send_command():
    """
    Test sending a string command to the oscilloscope via a socket.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
        soc.connect(("127.0.0.1", 12345))
        osc_raw.send_command(soc, "test")
        print(osc_raw.query(soc))
