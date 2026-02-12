# !/usr/bin/env python3

# ----------------------------------------------------------------------
# Name:        diffractio_init.py
# Purpose:     Initialization for diffractio package
#
# Author:      Luis Miguel Sanchez Brea
#
# Created:     2024
# Licence:     GPLv3
# ----------------------------------------------------------------------


"""Top-level package for Python Scalar and vector diffraction and interference.

Diffractio: A scientific computing package for Scalar and Vector Optical Interference and Diffraction in Python.
==================================================================================================================


"""

import datetime
import multiprocessing

import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
from matplotlib import cm, rcParams

__author__ = """Luis Miguel Sanchez Brea"""
__email__ = "optbrea@ucm.es"
__version__ = "1.0.0"
name = "diffractio"

um = 1.0
mm = 1000.0 * um
nm = um / 1000.0
degrees = np.pi / 180.0
s = 1.0
seconds = 1.0

eps = 1e-6
num_decimals = 4

no_date = False  # for test

now = datetime.datetime.now()
date_test = now.strftime("%Y-%m-%d_%H")

num_max_processors = multiprocessing.cpu_count()

rcParams["figure.dpi"] = 75
