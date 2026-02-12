"""
Vector field implementations.

vector/
├── __init__.py        # Exports vector field modules.
├── x_field.py         # 1D vector fields (X).
├── xy_field.py        # 2D vector fields (XY).
├── xy_mask.py         # 2D vector masks (XY).
├── xy_source.py       # 2D vector sources (XY).
├── xz_field.py        # 2D vector fields (XZ).
├── xz_field_backup.py # Backup of XZ vector fields.
├── xyz_field.py       # 3D vector fields (XYZ).
└── z_field.py         # 1D vector fields (Z).
"""

from . import x_field
from . import xy_field
from . import xy_mask
from . import xy_source
from . import xz_field
from . import xyz_field
from . import z_field
