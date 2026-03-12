# !/usr/bin/env python3

"""Smoke tests for Vector_field_XZ"""

import datetime
import os

import numpy as np

from diffractio import no_date, um
from diffractio.vector.xz_field import Vector_field_XZ

if no_date is True:
    date = "0"
else:
    now = datetime.datetime.now()
    date = now.strftime("%Y-%m-%d_%H")

path_base = "test_results"
path_class = "vector_fields_XZ"

newpath = f"{path_base}/{date}/{path_class}/"

if not os.path.exists(newpath):
    os.makedirs(newpath)


class Test_Vector_fields_XZ:
    def test_instantiation(self):
        """Test that Vector_field_XZ can be instantiated with small grids."""
        x = np.linspace(-50 * um, 50 * um, 16)
        z = np.linspace(0, 100 * um, 16)
        wavelength = 0.6328 * um

        EM = Vector_field_XZ(x=x, z=z, wavelength=wavelength)
        assert EM.type == "Vector_field_XZ"
        assert EM.wavelength == wavelength
        assert EM.Ex.shape == (len(z), len(x))
        assert EM.Ey.shape == (len(z), len(x))
        assert EM.Ez.shape == (len(z), len(x))

    def test_intensity(self):
        """Test that intensity returns a real-valued array of correct shape."""
        x = np.linspace(-50 * um, 50 * um, 16)
        z = np.linspace(0, 100 * um, 16)
        wavelength = 0.6328 * um

        EM = Vector_field_XZ(x=x, z=z, wavelength=wavelength)
        EM.Ex = np.ones_like(EM.Ex)

        intensity = EM.intensity()
        assert intensity.shape == (len(z), len(x))
        assert np.all(np.isreal(intensity))
        assert np.all(intensity >= 0)

    def test_duplicate(self):
        """Test that duplicate creates an independent copy."""
        x = np.linspace(-50 * um, 50 * um, 16)
        z = np.linspace(0, 100 * um, 16)
        wavelength = 0.6328 * um

        EM = Vector_field_XZ(x=x, z=z, wavelength=wavelength)
        EM.Ex = np.ones_like(EM.Ex)

        EM2 = EM.duplicate()
        assert EM2.type == EM.type
        assert np.array_equal(EM2.Ex, EM.Ex)

        # Verify independence
        EM2.Ex[0, 0] = 999
        assert EM.Ex[0, 0] != 999

    def test_clear_field(self):
        """Test that clear_field zeros out the field components."""
        x = np.linspace(-50 * um, 50 * um, 16)
        z = np.linspace(0, 100 * um, 16)
        wavelength = 0.6328 * um

        EM = Vector_field_XZ(x=x, z=z, wavelength=wavelength)
        EM.Ex = np.ones_like(EM.Ex)
        EM.Ey = np.ones_like(EM.Ey)

        EM.clear_field()
        assert np.all(EM.Ex == 0)
        assert np.all(EM.Ey == 0)
        assert np.all(EM.Ez == 0)
