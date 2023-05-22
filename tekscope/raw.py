"""
Low-level functions for interacting with the oscilloscope's socket server.
"""

import socket


def send_command(soc: socket.socket, command: str):
    """
    Sends a string command to the oscilloscope.
    """
    soc.sendall(f"{command}\n".encode("utf-8"))


def query_ascii(soc: socket.socket) -> bytes:
    """
    Queries ASCII output data from the oscilloscope in response to a command.

    Reads to the next newline.
    """
    ret = b""
    data = soc.recv(1)
    while data != b"\n":
        ret += data
        data = soc.recv(1)
    return ret

def query_binary(soc: socket.socket) -> bytes:
    """
    Queries binary data from the oscilloscope in response to a command.

    Reads according to the IEEE488.2 binary block format.
    """
    header = soc.recv(2)
    assert header[0] == ord("#")
    digits = int(chr(header[1]))
    length = int(soc.recv(digits))
    data = soc.recv(length)
    soc.recv(1) # Receive and discard final newline
    return data


# pylint: disable-next=too-few-public-methods
class AcquireState:
    """
    Available options for the ACQUIRE:STATE command.
    """

    RUN = "RUN"
    STOP = "STOP"


def acquire_state_cmd(state: str) -> str:
    """
    Starts or stops acquisitions.
    """
    return f"ACQUIRE:STATE {state}"


def acquire_numacq_cmd() -> str:
    """
    Returns the number of waveform acquisitions that have occured.
    """
    return "ACQUIRE:NUMACQ?"


def acquire_numsequence_cmd(num: int) -> str:
    """
    Sets or returns the number of acquisitions used in the sequence.
    """
    return f"ACQUIRE:SEQUENCE:NUMSEQUENCE {num}"


# pylint: disable-next=too-few-public-methods
class AcquireStopAfter:
    """
    Available options for the ACQUIRE:STOPAFTER command.
    """

    RUNSTOP = "RUNSTOP"
    SEQUENCE = "SEQUENCE"


def acquire_stopafter_cmd(stopafter: str) -> str:
    """
    Specifies whether the oscilloscope should continually acquire acquisitions
    or acquire only a single sequence.
    """
    return f"ACQUIRE:STOPAFTER {stopafter}"


# pylint: disable-next=too-few-public-methods
class AnalogSource:
    """
    Available analog source channels.
    """

    CH1 = "CH1"
    CH2 = "CH2"
    CH3 = "CH3"
    CH4 = "CH4"
    SOURCES = [CH1, CH2, CH3, CH4]

    @staticmethod
    def is_valid(source: str) -> bool:
        """
        Returns whether the given source is a valid digital source.
        """
        return source in AnalogSource.SOURCES


# pylint: disable-next=too-few-public-methods
class DigitalSource:
    """
    Available digital source channels.
    """

    D0 = "D0"
    D1 = "D1"
    D2 = "D2"
    D3 = "D3"
    D4 = "D4"
    D5 = "D5"
    D6 = "D6"
    D7 = "D7"
    D8 = "D8"
    D9 = "D9"
    D10 = "D10"
    D11 = "D11"
    D12 = "D12"
    D13 = "D13"
    D14 = "D14"
    D15 = "D15"
    SOURCES = [D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, D14, D15]

    @staticmethod
    def is_valid(source: str) -> bool:
        """
        Returns whether the given source is a valid digital source.
        """
        return source in DigitalSource.SOURCES



def data_source_cmd(state: str) -> str:
    """
    Specifies source waveform to be transferred from the oscilloscope.
    """
    return f"DATA:SOURCE {state}"


def data_start_cmd(start: int) -> str:
    """
    Specifies starting data point for waveform transfer.
    """
    return f"DATA:START {start}"


def data_stop_cmd(stop: int) -> str:
    """
    Specifies final data point for waveform transfer.
    """
    return f"DATA:STOP {stop}"


# pylint: disable-next=too-few-public-methods
class DataEncdg:
    """
    Available data encodings.
    """

    ASCII = "ASCII"
    BINARY = "BINARY"


def data_encdg_cmd(encdg: str) -> str:
    """
    Specifies data encoding format for waveform transfer.
    """
    if encdg == DataEncdg.BINARY:
        return "DATA:ENCDG RIBINARY"
    return "DATA:ENCDG ASCII"


def data_width_cmd(width: int) -> str:
    """
    Specifies data width for waveform transfer.
    """
    return f"DATA:WIDTH {width}"


def wfmoutpre_cmd() -> str:
    """
    Queries metadata of the waveform to be transferred.
    """
    return "WFMOUTPRE?"


def header_cmd(header: bool) -> str:
    """
    Toggles headers in oscilloscope responses.
    """
    return f"HEADER {int(header)}"


def curve_cmd() -> str:
    """
    Initiates data transfer from oscilloscope to computer.
    """
    return "CURVE?"


def clear_cmd() -> str:
    """
    Clears existing acquisitions.
    """
    return "CLEAR"


def select_cmd(source: str, enable: bool):
    """
    Enables or disables a source channel on the oscilloscope display.
    """
    selector = "ON" if enable else "OFF"
    return f"SELECT:{source} {selector}"


def idn() -> str:
    """
    Queries the identity of the oscilloscope.
    """
    return "*idn?"
