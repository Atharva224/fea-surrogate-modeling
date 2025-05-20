from ansys.mapdl.core import launch_mapdl
import numpy as np
import pandas as pd
import os

# Launch MAPDL
exec_path = r"C:\Program Files\ANSYS Inc\ANSYS Student\v242\ansys\bin\winx64\ansys242.exe"
mapdl = launch_mapdl(exec_file=exec_path, run_location=".", override=True, mode="grpc")

# Param ranges
E_list = np.linspace(100e9, 250e9, 5)          # Young’s modulus in Pa
force_list = np.linspace(500, 2000, 5)         # Force in N
hole_radius_list = np.linspace(0.005, 0.025, 5)  # Hole radius from 0.5 cm to 2.5 cm

# Plate dimensions
length, height, thickness = 0.1, 0.1, 0.01  # 10 cm plate
nu = 0.3

results = []

for E in E_list:
    for force in force_list:
        for hole_radius in hole_radius_list:
            try:
                mapdl.clear()
                mapdl.prep7()

                # Material
                mapdl.mp('EX', 1, E)
                mapdl.mp('PRXY', 1, nu)

                # Element type
                mapdl.et(1, 'PLANE183')
                mapdl.keyopt(1, 3, 3)  # Plane stress with thickness
                mapdl.r(1, thickness)


#Keeping the original work safe. Email atharvasinnarkar@gmail.com for the file and mention the proper usecase.
