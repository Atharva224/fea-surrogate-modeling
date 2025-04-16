import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load your dataset
df = pd.read_csv("fea_dataset_with_hole.csv")

# Extract values
X = df["Force"]
Y = df["Hole_Radius"]
Z = df["Max_Displacement"]

# Create figure
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# 3D scatter plot
sc = ax.scatter(X, Y, Z, c=Z, cmap='plasma', s=60)

# Labels and title
ax.set_xlabel("Force (N)", labelpad=15)
ax.set_ylabel("Hole Radius (m)", labelpad=15)
ax.set_zlabel("Max Displacement (m)", labelpad=15)
ax.set_title("Displacement Response to Force and Hole Radius", pad=20)

# Color bar for displacement levels
cbar = plt.colorbar(sc, pad=0.1, shrink=0.6)
cbar.set_label("Displacement Level (m)")

# Clean formatting
ax.tick_params(axis='both', which='major', labelsize=10)
ax.grid(True)

plt.tight_layout()
plt.show()
