# 🧠 FEA Surrogate Modeling

This project demonstrates how to replace expensive Finite Element Analysis (FEA) simulations with a fast and accurate machine learning model. A plate with and without a central hole is simulated using Ansys MAPDL via Python, and AI models are trained to predict stress and displacement from input parameters like force, material properties, and geometry.

---

## 🎯 Objectives

- ✅ Automate FEA simulations using Ansys MAPDL (PyMAPDL)
- ✅ Generate datasets by varying force, Young’s modulus, and hole radius
- ✅ Train surrogate ML models (Random Forest Regressors)
- ✅ Visualize model accuracy and structural response
- ✅ Predict stress and displacement instantly without rerunning Ansys

---

## 🛠️ Tools & Technologies

| Area               | Tool/Library         |
|--------------------|----------------------|
| FEA Solver         | Ansys MAPDL (via PyMAPDL) |
| Programming        | Python               |
| ML Algorithms      | scikit-learn (Random Forest) |
| Data Processing    | pandas, NumPy        |
| Visualization      | matplotlib           |

---

## 📊 Sample Outputs

### Displacement Response Surface  
![Displacement](Displacement%20response%20to%20force%20and%20hole%20radius.png)

### Stress Response Surface  
![Stress](Visualizing%20Stress%20vs%20Force%20&%20Hole%20Radius.png)

---

## 📈 Model Performance

| Output         | R² Score |
|----------------|----------|
| Displacement   | ~0.936   |
| Stress         | ~0.9997  |

---

## 🧠 How It Works

1. Parametric FEA simulations are run using Python and Ansys.
2. Results (max stress and displacement) are saved into CSV files.
3. ML models learn to predict these results from the input parameters:
   - Young’s modulus
   - Applied force
   - Hole radius
4. Once trained, predictions are nearly instantaneous — no solver needed!

---

## 🚀 Future Ideas

- Add Streamlit app for real-time prediction
- Train neural networks (PyTorch)
- Support more complex geometries
- Add inverse prediction: "what design gives max stress under X?"

---

## 📬 Author

**Atharva Sinnarkar**  
MSc Simulation & Modeling  
[GitHub Profile](https://github.com/Atharva224)

---

## 📜 License

MIT License
