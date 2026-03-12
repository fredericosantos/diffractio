# !/usr/bin/env python3

"""Smoke tests for Vector_field_Z"""

import datetime
import os

import numpy as np

from diffractio import no_date, um
from diffractio.vector.z_field import Vector_field_Z

if no_date is True:
    date = "0"
else:
    now = datetime.datetime.now()
    date = now.strftime("%Y-%m-%d_%H")

path_base = "test_results"
path_class = "vector_fields_Z"

newpath = f"{path_base}/{date}/{path_class}/"

if not os.path.exists(newpath):
    os.makedirs(newpath)


class Test_Vector_fields_Z:
    def test_instantiation(self):
        """Test that Vector_field_Z can be instantiated."""
        z = np.linspace(0, 100 * um, 32)
        wavelength = 0.6328 * um

        EM = Vector_field_Z(z=z, wavelength=wavelength)
        assert EM.type == "Vector_field_Z"
        assert EM.wavelength == wavelength
        assert EM.Ex.shape == (len(z),)
        assert EM.Ey.shape == (len(z),)
        assert EM.Ez.shape == (len(z),)

    def test_intensity(self):
        """Test that intensity returns a real-valued array of correct shape."""
        z = np.linspace(0, 100 * um, 32)
        wavelength = 0.6328 * um

        EM = Vector_field_Z(z=z, wavelength=wavelength)
        EM.Ex = np.ones_like(EM.Ex)

        intensity = EM.intensity()
        assert intensity.shape == (len(z),)
        assert np.all(np.isreal(intensity))
        assert np.all(intensity >= 0)

    def test_duplicate(self):
        """Test that duplicate creates an independent copy."""
        z = np.linspace(0, 100 * um, 32)
        wavelength = 0.6328 * um

        EM = Vector_field_Z(z=z, wavelength=wavelength)
        EM.Ex = np.ones_like(EM.Ex)

        EM2 = EM.duplicate()
        assert EM2.type == EM.type
        assert np.array_equal(EM2.Ex, EM.Ex)

        # Verify independence
        EM2.Ex[0] = 999
        assert EM.Ex[0] != 999

    def test_clear_field(self):
        """Test that clear_field zeros out the field components."""
        z = np.linspace(0, 100 * um, 32)
        wavelength = 0.6328 * um

        EM = Vector_field_Z(z=z, wavelength=wavelength)
        EM.Ex = np.ones_like(EM.Ex)
        EM.Ey = np.ones_like(EM.Ey)

        EM.clear_field()
        assert np.all(EM.Ex == 0)
        assert np.all(EM.Ey == 0)
        assert np.all(EM.Ez == 0)
