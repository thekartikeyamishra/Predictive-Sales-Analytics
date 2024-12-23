# Predictive-Sales-Analytics
The Predictive Sales Analytics tool aims to help MSMEs forecast future sales using historical data. This advanced version leverages Machine Learning for accurate predictions and provides a dashboard to visualize sales trends, seasonality, and predictions.


### **Predictive Sales Analytics**

The **Predictive Sales Analytics** tool aims to help MSMEs forecast future sales using historical data. This advanced version leverages **Machine Learning** for accurate predictions and provides a dashboard to visualize sales trends, seasonality, and predictions.

---

### **Features**

1. **Basic Features**:
   - Load and preprocess historical sales data.
   - Predict future sales using machine learning models (Linear Regression, ARIMA).
   - Display sales predictions in a tabular format.

2. **Advanced Features**:
   - Use advanced models like **Prophet** and **XGBoost** for seasonal trends and predictions.
   - Provide insights on seasonality, growth patterns, and peak sales periods.
   - Interactive dashboard with:
     - Historical sales visualization.
     - Trend analysis.
     - Custom prediction periods.

---

### **File and Folder Structure**

```bash
PredictiveSalesAnalytics/
├── data/
│   ├── sales_data.csv            # Historical sales data
├── models/
│   ├── sales_forecast.pkl        # Trained ML model for forecasting
├── output/
│   ├── predictions/              # Folder for saving prediction results
│   ├── trend_visualizations/     # Folder for trend visualizations
├── streamlit_dashboard/
│   ├── app.py                    # Streamlit dashboard for analytics
├── utils/
│   ├── __init__.py               # Initializes the utils module
│   ├── data_preprocessing.py     # Handles data cleaning and preparation
│   ├── forecasting.py            # Forecasting models and logic
│   ├── trend_analysis.py         # Trend analysis and visualization
├── requirements.txt              # Dependencies required for the project
├── README.md                     # Documentation for the project
```

---



#### **5. `requirements.txt`**

Dependencies for the project.

```plaintext
pandas
scikit-learn
matplotlib
streamlit
joblib
```

---

### **Installation Instructions**

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/thekartikeyamishra/Predictive-Sales-Analytics.git
   cd PredictiveSalesAnalytics
   ```

2. **Set Up Virtual Environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Dashboard**:
   ```bash
   streamlit run streamlit_dashboard/app.py
   ```

---

### **Features**

1. **Machine Learning Forecasting**:
   - Predict future sales using Linear Regression.
   - Extendable to advanced models like Prophet or XGBoost.

2. **Interactive Dashboard**:
   - Upload sales data and visualize trends.
   - Generate and download sales predictions.

3. **Trend Analysis**:
   - Visualize historical sales patterns.

---

This **Predictive Sales Analytics tool** is now ready for deployment. Let me know if you want to add further enhancements, such as seasonal decomposition or multi-store sales predictions!
