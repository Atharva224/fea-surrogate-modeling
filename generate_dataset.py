from ansys.mapdl.core import launch_mapdl
import numpy as np
import pandas as pd

# Setup MAPDL path
exec_path = r"C:\Program Files\ANSYS Inc\ANSYS Student\v242\ansys\bin\winx64\ansys242.exe"
mapdl = launch_mapdl(exec_file=exec_path, run_location=".", override=True, mode="grpc")

# Param ranges
E_list = np.linspace(100e9, 250e9, 10)          # Young's modulus in Pa
force_list = np.linspace(500, 2000, 10)          # Force in N

# Geometry/material
length, height, thickness = 0.1, 0.1, 0.01
nu = 0.3

results = []

for E in E_list:
    for force in force_list:
        mapdl.clear()
        mapdl.prep7()

        # Material
        mapdl.mp('EX', 1, E)
        mapdl.mp('PRXY', 1, nu)


#Keeping the original work safe. Email atharvasinnarkar@gmail.com for the file and mention the proper usecase.
