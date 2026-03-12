# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

Diffractio is a Python library for scalar and vector diffraction/interference simulation in optics. Originally by Luis Miguel Sanchez Brea (UCM), now maintained as a fork with modernized tooling (uv, ruff, ty, Python 3.13+).

## Commands

```bash
uv sync                          # Install dependencies
uv run pytest                    # Run all tests
uv run pytest tests/test_scalar_fields_XY.py  # Run single test file
uv run pytest -k "test_name"     # Run single test by name
uv run pytest -m slow            # Run only slow-marked tests
uv run ruff check .              # Lint
uv run ruff check --fix .        # Auto-fix lint issues
uv run ruff format .             # Format
uv run ty check .                # Type check
```

## Architecture

### Class Hierarchy

Fields are organized by dimensionality (X, XY, XZ, XYZ, Z) and type (scalar vs vector). Each dimension has independent base classes — there is no shared abstract base.

```
Scalar_field_{X,XY,XZ,XYZ,Z}    # Base field classes (complex amplitude on a grid)
  ├── Scalar_source_{X,XY}       # Incident wave generators (inherit from field)
  └── Scalar_mask_{X,XY,XZ,XYZ}  # Amplitude/phase modulators (inherit from field)

Vector_field_{X,XY,XZ,XYZ,Z}    # Vector fields with Ex, Ey components
  ├── Vector_source_XY
  └── Vector_mask_XY
```

**Field attributes**: `x` (and `y`, `z` as needed), `wavelength`, `u` (complex array for scalar) or `Ex`/`Ey` (for vector), `n_background`.

### Package Layout

- **`diffractio/core/`** — Shared utilities used across all field types:
  - `math.py` — FFT helpers (Bluestein DFT), distance, nearest-point, extrema finding
  - `operations.py` — Field arithmetic (`add`, `sub`, `rmul`), save/load, oversampling, `duplicate()`
  - `optics.py` — Beam analysis (FWHM, beam width, DOF), MTF, roughness, refractive index
  - `drawing.py` / `drawing3D.py` — Visualization (2D/3D plots, video generation)
- **`diffractio/scalar/`** — Scalar field implementations (~644KB, largest module)
  - `xy_field.py` is the most feature-rich (126KB) with FFT, RS, CZT propagation
- **`diffractio/vector/`** — Vector field implementations with polarization support
  - Adds Stokes parameters, Jones/py_pol interop, Poynting vectors
- **`diffractio/utils/`** — Multiprocessing helpers, DXF export, test utilities
- **`diffractio/config.py`** — Drawing config (`CONF_DRAWING`), type literals for draw options, operation options

### Propagation Algorithms

Scalar: `fft()`, `ifft()`, `RS()` (Rayleigh-Sommerfeld), `CZT()` (Chirp Z-Transform)
Vector: `VFFT()`, `IVFFT()`, `VRS()`, `VCZT()` — vector equivalents

### Just-Init Convention

All `__init__.py` files follow the just-init pattern: one-line description + file tree listing with brief descriptions. Update these when adding/renaming files.

## Configuration

- `ruff`: line-length 100, google docstring convention, extensive rule set (see `pyproject.toml`)
- `ty`: strict on unresolved references/imports
- `pytest`: markers `slow`, `integration`, `unit`; strict mode; testpaths = `tests/`
- Drawing config in `config.py`: color maps, percentage thresholds, exception flags
