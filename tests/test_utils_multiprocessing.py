# !/usr/bin/env python3


# -------------------------------------------------------------------------------
# Name:       scalar_fields_XZ.py
# Purpose:    tests
#
# Author:    Luis Miguel Sanchez Brea
#
# Created:    2017
# Copyright:
# Licence:    GPL
# -------------------------------------------------------------------------------
import datetime
import os
import time

import numpy as np

from diffractio import no_date
from diffractio.utils.multiprocessing import auxiliar_multiprocessing

if no_date is True:
    date = "0"
else:
    now = datetime.datetime.now()
    date = now.strftime("%Y-%m-%d_%H")

path_base = "test_results"
path_class = "utils_math"

newpath = f"{path_base}/{date}/{path_class}/"

if not os.path.exists(newpath):
    os.makedirs(newpath)


def function_to_test(iterable, constant):
    return iterable**2 * constant


class Test_utils_math:
    def test_distance(self):

        N = 50000
        variable_process = np.linspace(0, 1, N)
        start = time.time()
        sc = auxiliar_multiprocessing()
        sc.execute_multiprocessing(function_to_test, variable_process, 1, 8)
        # print("{}".format(np.array(sc.result)))
        print(f"8 processes pool took {time.time() - start} seconds")
        start = time.time()
        res = np.zeros(N)
        for ind, val in enumerate(variable_process):
            res[ind] = function_to_test(val, 1)
        print(f"Single process pool took {time.time() - start} seconds")

        assert True
