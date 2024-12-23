import streamlit as st
from utils.data_preprocessing import process_sales_data
from utils.forecasting import train_forecast_model, save_model, predict_future_sales
from utils.trend_analysis import plot_historical_trends

st.title("Predictive Sales Analytics")
uploaded_file = st.file_uploader("Upload Historial Sales Data (CSV)", type=["csv"])

if uploaded_file:
    st.subheader("Processing Data...")
    data = process_sales_data(uploaded_file)

    st.subheader("Historial Sales Trends")
    plot_historical_trends(data)
    st.image("output/trend_visualizations/trends.png", caption="Sales Trends")

    st.subheader("Training Forecasting Model...")
    model, X_test, y_test = train_forecast_model(data)
    save_model(model)

    st.subheader("Predict Future Sales")
    future_periods = st.number_input("Enter Number of Future Periods to Predict", main_value=1, max_value=365, value=30)
    predictions = predict_future_sales(model, future_periods)

    st.write("Future Sales Predictions:")
    st.write(predictions)

    st.download_button("Download Predictions", "\n".join(map(str,predictions)), file_name="predictions.csv")

