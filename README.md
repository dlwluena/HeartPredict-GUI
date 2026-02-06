## HeartPredict AI: Clinical Diagnosis Support System

An advanced Artificial Neural Network (ANN) expert system designed to predict cardiovascular disease risk with high precision. This project bridges the gap between deep learning research and end-user accessibility through a modern, interactive dashboard.

## Overview
The HeartPredict AI system processes 13 specific clinical parameters (e.g., age, cholesterol levels, EKG results) to calculate a patient's risk probability. Unlike traditional linear models, this system utilizes a non-linear Deep Learning architecture to capture complex medical patterns.

## Demo & Usage Example

Below is a sample prediction based on a hypothetical patient scenario. This demonstration shows how the AI model processes medical parameters to assess cardiovascular risk.

### **Sample Patient Profile**
| Feature | Value | Feature | Value |
| :--- | :--- | :--- | :--- |
| **Age** | 25 | **Max Heart Rate** | 156 |
| **Sex** | 0 (Female) | **Exercise Angina** | 0 (No) |
| **Chest Pain Type** | 1 | **Oldpeak** | 5.6 |
| **Rest Blood Pressure**| 78 | **ST Slope** | 2 |
| **Cholesterol** | 178 | **Vessels (CA)** | 2 |
| **Fasting Blood Sugar**| 1 | **Thal Result** | 6 |
| **Rest ECG** | 2 | | |

### **Prediction Result**
The dashboard visualizes the AI's analysis in real-time. For the parameters above, the model predicted:
**Condition Normal: 16.5% Risk Probability**

<img width="592" height="890" alt="image" src="https://github.com/user-attachments/assets/9b53ca80-a019-496b-a88a-c726afc032ef" />


## Key Achievements:

* **Accuracy:** Achieved 90.00% test accuracy.
* **Optimization:** Minimized overfitting using L2 Regularization (λ=0.01).
* **GUI:** Fully responsive medical dashboard built with PySide6.
* **Search:** Optimized hyperparameters via Random Search cross-validation.

## Model Architecture (ANN)
The system is built on a Multi-Layer Perceptron (MLP) architecture:

* **Input Layer:** 13 Neurons (Standardized clinical features).
* **Hidden Layer 1:** 16 Neurons (ReLU activation).
* **Hidden Layer 2:** 8 Neurons (ReLU activation).
* **Output Layer:** 1 Neuron (Sigmoid activation for probability).

## Performance Metrics
The model was evaluated using a Confusion Matrix to ensure clinical reliability:

* **Sensitivity (Recall):** High ability to detect positive heart disease cases.
* **Precision:** Low false-positive rate to prevent unnecessary patient anxiety.
* **F1-Score:** Balanced performance across both healthy and at-risk classes.

## Tech Stack

* **Core:** Python 3.13
* **Deep Learning:** TensorFlow 2.x, Keras
* **Data Analysis**: Pandas, NumPy, Scikit-learn
* **UI Framework:** PySide6 (Qt for Python)
* **Documentation:** LaTeX (Mathematical reporting)

## Project Structure
```plaintext
├── main.ipynb          # ANN Training, Optimization & Evaluation
├── gui.py              # PySide6 Desktop Application
├── heart_model.keras   # Saved Trained Neural Network
├── scaler.pkl          # Feature scaling parameters
├── feature_info.txt    # Detailed Clinical Data Guide
└── requirements.txt    # Dependency list
```

## How to Use
**1. Installation:**
```bash
pip install -r requirements.txt
```
**2. Launch the System:**
```bash
python gui.py
```
## How to Run

1. Clone the repo: `git clone https://github.com/dlwluena/HeartPredict-GUI.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the dashboard: `python gui.py`

## Performance Analysis
In medical prognosis, accuracy is not the only metric. We focus on the Confusion Matrix to minimize "False Negatives," ensuring that high-risk patients are not overlooked by the system.

## Medical Disclaimer
This tool is for educational and research purposes only. It should not be used as a replacement for professional medical diagnosis or treatment.
