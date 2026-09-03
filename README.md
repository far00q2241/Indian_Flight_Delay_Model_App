# ✈️ Flight Delay Prediction

A Machine Learning project that predicts whether a flight will be **Delayed** or **On Time**.

## 📌 Project Overview

This project uses flight schedule, airline, airport, weather, and operational data to predict flight delays.

### Dataset

* 150,000 flight records
* Target: `Delay_Target`
* `0` → On Time
* `1` → Delayed

## 🤖 Models Used

* Logistic Regression
* Decision Tree
* Random Forest
* Gradient Boosting
* XGBoost

## 🏆 Best Model

**Random Forest Classifier**

### Performance

* Accuracy: **91.74%**
* Balanced Accuracy: **83.92%**
* F1 Score: **95.20%**
* ROC-AUC: **86.21%**
* PR-AUC: **95.97%**

## 🔧 Technologies

* Python
* Pandas
* NumPy
* Scikit-learn
* XGBoost
* Joblib
* Streamlit

## 🚀 Streamlit App

The project includes a Streamlit application where users can enter flight details and get a prediction.

**Prediction:**

* ✈️ Delayed
* ✅ On Time

## 📁 Files

```text
Flight_Delay_Prediction/
│
├── app.py
├── flight_delay_model.pkl
├── flight_delay_columns.pkl
├── requirements.txt
└── README.md
```

## ▶️ Run the App

```bash
pip install -r requirements.txt
streamlit run app.py
```

## 👨‍💻 Author

**Mohammed Farooq Khan**

GitHub: https://github.com/far00q2241
