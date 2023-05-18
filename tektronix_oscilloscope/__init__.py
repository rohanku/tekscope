"""
API for interfacing with a Tektronix oscilloscope.
"""

import socket
from .raw import *
from .parse import *


class Oscilloscope:
    """
    Class with high-level utilties for connecting to and remotely
    controlling a Tektronix oscilloscope.
    """

    def __init__(self, host="169.254.8.194", port=4000):
        self.soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.soc.connect((host, port))
        send_command(self.soc, header_cmd(False))

    def start_acquire(self):
        """
        Starts an acquisition.
        """
        send_command(self.soc, acquire_state_cmd(AcquireState.RUN))

    def stop_acquire(self):
        """
        Stops an acquisition.
        """
        send_command(self.soc, acquire_state_cmd(AcquireState.STOP))

    def acquire_analog_sequence(self, num_acq: int, source: str) -> [int]:
        """
        Acquires an analog sequence of the given length and parses it as a Python list.
        """
        send_command(self.soc, select_cmd(source, True))
        send_command(self.soc, acquire_numsequence_cmd(num_acq))
        send_command(self.soc, acquire_stopafter_cmd(AcquireStopAfter.SEQUENCE))
        send_command(self.soc, acquire_state_cmd(AcquireState.RUN))
        send_command(self.soc, data_source_cmd(source))
        send_command(self.soc, data_start_cmd(1))
        send_command(self.soc, data_stop_cmd(num_acq))
        send_command(self.soc, data_width_cmd(1))
        send_command(self.soc, data_encdg_cmd(DataEncdg.ASCII))
        send_command(self.soc, "*OPC?")
        query(self.soc)
        send_command(self.soc, curve_cmd())
        return parse_ascii_seq(query(self.soc))
