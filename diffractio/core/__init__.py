"""
Core functionality for Diffractio.

core/
├── __init__.py        # Exports math, optics, drawing, operations.
├── drawing.py         # 2D drawing utilities.
├── drawing3D.py       # 3D drawing utilities.
├── math.py            # Mathematical functions.
├── operations.py      # Common operations (load, save, get_size).
└── optics.py          # Optical utility functions.
"""

from . import drawing, drawing3D, math, operations, optics
