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

        # Element
        mapdl.et(1, 'PLANE183')
        mapdl.keyopt(1, 3, 3)
        mapdl.r(1, thickness)

        # Geometry and mesh
        mapdl.blc4(0, 0, length, height)
        mapdl.esize(0.01)
        mapdl.amesh("ALL")

        # Boundary conditions
        mapdl.nsel("S", "LOC", "X", 0)
        mapdl.d("ALL", "ALL")
        mapdl.nsel("S", "LOC", "X", length)
        pressure = force / (height * thickness)
        mapdl.sf("ALL", "PRES", pressure)
        mapdl.allsel()

        # Solve
        mapdl.run("/SOLU")
        mapdl.antype("STATIC")
        mapdl.solve()
        mapdl.finish()

        # Post-processing
        mapdl.post1()
        mapdl.set(1)

        disp = mapdl.post_processing.nodal_displacement("X")
        stress = mapdl.post_processing.element_stress("EQV")

        max_disp = np.max(np.abs(disp))
        max_stress = np.max(np.abs(stress))

        print(f"E={E:.1e}, F={force} -> Umax={max_disp:.2e} m, Smax={max_stress:.2e} Pa")

        # Save results
        results.append([E, force, max_disp, max_stress])

# Convert to DataFrame
df = pd.DataFrame(results, columns=["Youngs_Modulus", "Force", "Max_Displacement", "Max_Stress"])
df.to_csv("fea_dataset.csv", index=False)

print("Dataset saved to fea_dataset.csv")

mapdl.exit()
