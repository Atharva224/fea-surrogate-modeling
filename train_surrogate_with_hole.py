import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("fea_dataset_with_hole.csv")

# Inputs and Outputs
X = df[["Youngs_Modulus", "Force", "Hole_Radius"]]
y_disp = df["Max_Displacement"]
y_stress = df["Max_Stress"]

# Train/test split
X_train, X_test, y_disp_train, y_disp_test = train_test_split(X, y_disp, test_size=0.2, random_state=42)
_, _, y_stress_train, y_stress_test = train_test_split(X, y_stress, test_size=0.2, random_state=42)

# Train models
disp_model = RandomForestRegressor(n_estimators=100, random_state=42)
disp_model.fit(X_train, y_disp_train)

stress_model = RandomForestRegressor(n_estimators=100, random_state=42)
stress_model.fit(X_train, y_stress_train)

# Predictions
disp_pred = disp_model.predict(X_test)
stress_pred = stress_model.predict(X_test)

# Evaluation
print("Displacement R² Score:", r2_score(y_disp_test, disp_pred))
print("Stress R² Score:", r2_score(y_stress_test, stress_pred))

# Plot
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.scatter(y_disp_test, disp_pred, color='blue')
plt.xlabel("True Displacement")
plt.ylabel("Predicted Displacement")
plt.title("Displacement Prediction")

plt.subplot(1, 2, 2)
plt.scatter(y_stress_test, stress_pred, color='red')
plt.xlabel("True Stress")
plt.ylabel("Predicted Stress")
plt.title("Stress Prediction")

plt.tight_layout()
plt.show()
