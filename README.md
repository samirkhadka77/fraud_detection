#  Fraud Detection System

A machine learning-based fraud detection system that predicts whether a financial transaction is fraudulent or legitimate. This project uses an XGBoost pipeline and provides a simple **Streamlit web application** for real-time predictions.

---

##  Project Overview

Financial fraud detection is crucial for minimizing losses in banking and payment systems.  
This project uses a dataset of financial transactions to train a model that can detect fraudulent transactions with high accuracy. Users can input transaction details in a web interface and get real-time predictions.

---

##  Dataset

- **File:** `AIML_DATASET.csv`
- **Columns:**  
  - `step`, `type`, `amount`, `nameOrig`, `oldbalanceOrg`, `newbalanceOrig`, `nameDest`, `oldbalanceDest`, `newbalanceDest`, `isFraud`, `isFlaggedFraud`
- **Target column:** `isFraud`
- **Size:** ~ [insert number of rows if known]  

The dataset includes different types of transactions such as `PAYMENT`, `TRANSFER`, `CASH_OUT`, `DEBIT`, and `CASH_IN`.  

---

##  Technology & Tools Used

- Python 3.x
- Jupyter Notebook
- Pandas, NumPy
- Matplotlib, Seaborn
- Scikit-learn
- Streamlit
- Joblib

---

##  Exploratory Data Analysis (EDA)

Some key insights from the dataset:

- **Transaction Type Distribution:** `PAYMENT` and `CASH_OUT` are the most frequent.
- **Fraud Rate by Type:** Higher fraud rates in `TRANSFER` and `CASH_OUT` transactions.
- **Amount Analysis:** Log-transformed transaction amounts show skewness, with high-value outliers carefully analyzed.
- **Balance Differences:** Identified suspicious transactions where origin or destination balances went negative.
- **Correlation:** `amount` and balances correlate with fraud occurrence.

Visualizations like bar plots, histograms, boxplots, and heatmaps were used to better understand patterns.

---

##  Data Preprocessing

1. Removed irrelevant columns: `nameOrig`, `nameDest`, `isFlaggedFraud`.
2. Created new features:  
   - `balanceDiffOrig` = `oldbalanceOrg` - `newbalanceOrig`  
   - `balanceDiffDest` = `newbalanceDest` - `oldbalanceDest`
3. Handled categorical features (`type`) with One-Hot Encoding.
4. Standardized numerical features (`amount`, `oldbalanceOrg`, `newbalanceOrig`, `oldbalanceDest`, `newbalanceDest`) using `StandardScaler`.

---

## Model Training

- **Algorithm:** XGBoost / Logistic Regression pipeline (class imbalance handled)
- **Train/Test Split:** 70% train, 30% test with stratification
- **Pipeline:** Preprocessing + Classifier
- **Evaluation Metrics:**  
  - Accuracy, Precision, Recall, F1-score  
  - Confusion Matrix  
- Model was serialized using `joblib` as `fraud_detection_pipeline.pkl`.

---

## Streamlit Web App

The project includes a **Streamlit app** (`fraud_detection.py`) for real-time predictions.  

**Features:**
- User selects `Transaction Type`
- Inputs transaction details (`amount`, `oldbalanceOrg`, `newbalanceOrig`, `oldbalanceDest`, `newbalanceDest`)
- Click **Predict** to see if the transaction is `Fraudulent` or `Legitimate`

**Run Locally:**

```bash
# Install dependencies
pip install pandas scikit-learn streamlit joblib

# Run Streamlit app
streamlit run fraud_detection.py
