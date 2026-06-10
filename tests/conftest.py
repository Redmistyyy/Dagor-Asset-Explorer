"""Test fixtures and path setup."""
import sys
from os import path

# Make src/ importable so tests can do `from dae.util.xxx import yyy`
sys.path.insert(0, path.abspath(path.join(path.dirname(__file__), "..", "src")))
