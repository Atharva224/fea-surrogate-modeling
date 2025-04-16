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

# Meshing
mapdl.esize(0.01)
mapdl.amesh("ALL")

# Boundary condition: fix left edge
mapdl.nsel("S", "LOC", "X", 0)
mapdl.d("ALL", "ALL")

# Apply surface pressure on right edge
mapdl.nsel("S", "LOC", "X", length)
pressure = force / (height * thickness)  # N/m²
mapdl.sf("ALL", "PRES", pressure)
mapdl.allsel()

# Solution
mapdl.run("/SOLU")
mapdl.antype("STATIC")
mapdl.solve()
mapdl.finish()

# Post-processing
mapdl.post1()
mapdl.set(1)

# Use modern API to get displacements & stress
disp = mapdl.post_processing.nodal_displacement("X")
stress = mapdl.post_processing.element_stress("EQV")

max_disp = np.max(np.abs(disp))
max_stress = np.max(np.abs(stress))

# Output
print(f"Max displacement: {max_disp:.6e} m")
print(f"Max von Mises stress: {max_stress:.6e} Pa")

# Exit MAPDL
mapdl.exit()
