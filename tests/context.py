"""
Provides common context for tests.
"""

import os

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
BUILD_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "build")
os.makedirs(BUILD_DIR, exist_ok=True)
