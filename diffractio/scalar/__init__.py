"""
Scalar field implementations.

scalar/
├── __init__.py        # Exports scalar field modules.
├── x_field.py         # 1D scalar fields (X).
├── x_mask.py          # 1D scalar masks (X).
├── x_source.py        # 1D scalar sources (X).
├── xy_field.py        # 2D scalar fields (XY).
├── xy_mask.py         # 2D scalar masks (XY).
├── xy_source.py       # 2D scalar sources (XY).
├── xz_field.py        # 2D scalar fields (XZ).
├── xz_mask.py         # 2D scalar masks (XZ).
├── xyz_field.py       # 3D scalar fields (XYZ).
├── xyz_mask.py        # 3D scalar masks (XYZ).
└── z_field.py         # 1D scalar fields (Z).
"""

from . import x_field
from . import x_mask
from . import x_source
from . import xy_field
from . import xy_mask
from . import xy_source
from . import xz_field
from . import xz_mask
from . import xyz_field
from . import xyz_mask
from . import z_field
