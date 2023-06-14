"""
Tests of API for directly interacting with the oscilloscope's socket server.
"""

import socket
import pytest
from tekscope.raw import send_command, query_ascii


@pytest.mark.skip(reason="testing framework unimplemented")
def test_send_command():
    """
    Test sending a string command to the oscilloscope via a socket.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
        soc.connect(("127.0.0.1", 12345))
        send_command(soc, "test")
        print(query_ascii(soc))
