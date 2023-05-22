"""
Utilities for saving oscilloscope data to disk.
"""

import os
import pickle

def save_waveforms(waveforms: dict[str, [int]], out_path: str):
    with open(out_path, "wb") as f:
        f.write(pickle.dumps(waveforms))

def load_waveforms(in_path: str) -> dict[str, [int]]:
    with open(in_path, "rb") as f:
        return pickle.loads(f.read())
