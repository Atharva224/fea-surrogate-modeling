import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load dataset
df = pd.read_csv("fea_dataset_with_hole.csv")

# Extract variables
X = df["Force"]
Y = df["Hole_Radius"]
Z = df["Max_Stress"]

# Plot
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Scatter plot with color
sc = ax.scatter(X, Y, Z, c=Z, cmap='viridis', s=60)

# Axis labels with padding
ax.set_xlabel("Force (N)", labelpad=15)
ax.set_ylabel("Hole Radius (m)", labelpad=15)
ax.set_zlabel("Max von Mises Stress (Pa)", labelpad=15)
ax.set_title("Stress Response to Force and Hole Radius", pad=20)

# Add color bar to explain colors
cbar = plt.colorbar(sc, pad=0.1, shrink=0.6)
cbar.set_label("Stress Level (Pa)")

# Improve layout
ax.tick_params(axis='both', which='major', labelsize=10)
ax.grid(True)

plt.tight_layout()
plt.show()



