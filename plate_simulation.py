from ansys.mapdl.core import launch_mapdl
import numpy as np

# Correct path for your Student version
exec_path = r"C:\Program Files\ANSYS Inc\ANSYS Student\v242\ansys\bin\winx64\ansys242.exe"

# Launch MAPDL
mapdl = launch_mapdl(
    exec_file=exec_path,
    run_location=".",
    override=True,
    mode="grpc",
    loglevel="INFO",
    log_apdl=True
)

# Clean start
mapdl.clear()
mapdl.prep7()

# Problem setup
length = 0.1       # 10 cm
height = 0.1       # 10 cm
thickness = 0.01   # 1 cm
E = 200e9          # Young’s modulus (Pa)
nu = 0.3           # Poisson’s ratio
force = 1000       # Force (N)

# Material definition
mapdl.mp('EX', 1, E)
mapdl.mp('PRXY', 1, nu)

# Element definition
mapdl.et(1, 'PLANE183')
mapdl.keyopt(1, 3, 3)  # Plane stress with thickness
mapdl.r(1, thickness)

# Geometry
mapdl.blc4(0, 0, length, height)

#Keeping the original work safe. Email atharvasinnarkar@gmail.com for the file and mention the proper usecase.
