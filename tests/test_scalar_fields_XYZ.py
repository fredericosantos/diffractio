# !/usr/bin/env python3

"""Smoke tests for Scalar_field_XYZ"""

import datetime
import os

import numpy as np

from diffractio import no_date, um
from diffractio.scalar.xyz_field import Scalar_field_XYZ

if no_date is True:
    date = "0"
else:
    now = datetime.datetime.now()
    date = now.strftime("%Y-%m-%d_%H")

path_base = "test_results"
path_class = "scalar_fields_XYZ"

newpath = f"{path_base}/{date}/{path_class}/"

if not os.path.exists(newpath):
    os.makedirs(newpath)


class Test_Scalar_fields_XYZ:
    def test_instantiation(self):
        """Test that Scalar_field_XYZ can be instantiated with small grids."""
        x = np.linspace(-50 * um, 50 * um, 8)
        y = np.linspace(-50 * um, 50 * um, 8)
        z = np.linspace(0, 100 * um, 8)
        wavelength = 0.6328 * um

        field = Scalar_field_XYZ(x=x, y=y, z=z, wavelength=wavelength)
        assert field.type == "Scalar_field_XYZ"
        assert field.wavelength == wavelength
        assert field.u.shape == (len(y), len(x), len(z))

    def test_intensity(self):
        """Test that intensity returns a real-valued array of correct shape."""
        x = np.linspace(-50 * um, 50 * um, 8)
        y = np.linspace(-50 * um, 50 * um, 8)
        z = np.linspace(0, 100 * um, 8)
        wavelength = 0.6328 * um

        field = Scalar_field_XYZ(x=x, y=y, z=z, wavelength=wavelength)
        field.u = np.ones_like(field.u)

        intensity = field.intensity()
        assert intensity.shape == (len(y), len(x), len(z))
        assert np.all(np.isreal(intensity))
        assert np.all(intensity >= 0)

    def test_duplicate(self):
        """Test that duplicate creates an independent copy."""
        x = np.linspace(-50 * um, 50 * um, 8)
        y = np.linspace(-50 * um, 50 * um, 8)
        z = np.linspace(0, 100 * um, 8)
        wavelength = 0.6328 * um

        field = Scalar_field_XYZ(x=x, y=y, z=z, wavelength=wavelength)
        field.u = np.ones_like(field.u)

        field2 = field.duplicate()
        assert field2.type == field.type
        assert np.array_equal(field2.u, field.u)

        # Verify independence
        field2.u[0, 0, 0] = 999
        assert field.u[0, 0, 0] != 999

    def test_clear_field(self):
        """Test that clear_field zeros out the field."""
        x = np.linspace(-50 * um, 50 * um, 8)
        y = np.linspace(-50 * um, 50 * um, 8)
        z = np.linspace(0, 100 * um, 8)
        wavelength = 0.6328 * um

        field = Scalar_field_XYZ(x=x, y=y, z=z, wavelength=wavelength)
        field.u = np.ones_like(field.u)

        field.clear_field()
        assert np.all(field.u == 0)
