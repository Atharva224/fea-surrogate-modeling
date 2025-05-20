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

                # Geometry
                x_center = length / 2
                y_center = height / 2
                mapdl.blc4(0, 0, length, height)              # Plate
                mapdl.cyl4(x_center, y_center, hole_radius)   # Hole
                mapdl.asba(1, 2)                              # Subtract hole from plate

                # Mesh
                mapdl.esize(0.002)
                mapdl.amesh("ALL")

                # Boundary Conditions
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

                print(f"E={E:.1e}, F={force}, r={hole_radius:.3f} → Umax={max_disp:.2e} m, Smax={max_stress:.2e} Pa")
                results.append([E, force, hole_radius, max_disp, max_stress])

            except Exception as e:
                print(f"Error: E={E}, F={force}, r={hole_radius:.3f} - {e}")
                continue

# Save dataset
df = pd.DataFrame(results, columns=["Youngs_Modulus", "Force", "Hole_Radius", "Max_Displacement", "Max_Stress"])
csv_path = "fea_dataset_with_hole.csv"
df.to_csv(csv_path, index=False)

print(f"Dataset saved to {csv_path}")
mapdl.exit()
