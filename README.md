# 🛡️ Adaptive Network Traffic Anomaly Classification

A machine learning capstone project built to classify and detect network intrusions using the NSL-KDD dataset, deployed via an interactive Streamlit web interface.

## 🚀 Project Overview
This project acts as an AI security guard, filtering network flow parameters to accurately distinguish between legitimate traffic and malicious cyber attacks.

## 🛠️ Tech Stack & Tools
* **Language:** Python
* **Machine Learning:** Scikit-Learn (Decision Tree Classifier)
* **Data Processing:** Pandas, NumPy
* **Web UI:** Streamlit
* **Model Serialization:** Joblib

## 📊 Model Performance
* **Accuracy:** 75.6%
* **Precision:** 92.5%
* **Recall:** 62.2%
* **F1-Score:** 74.4%

## ⚙️ How to Run Locally
1. Clone the repository and navigate to the project folder.
2. Install dependencies: `pip install streamlit scikit-learn pandas joblib`
3. Launch the web app:
   ```bash
   streamlit run app.py
