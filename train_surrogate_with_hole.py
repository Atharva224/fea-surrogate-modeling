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

#Keeping the original work safe. Email atharvasinnarkar@gmail.com for the file and mention the proper usecase.
