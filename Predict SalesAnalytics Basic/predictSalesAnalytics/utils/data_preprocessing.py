import pandas as pd

def process_sales_data(data_path):
    data = pd.read_csv(data_path)
    data['Date'] = pd.to_datetime(data["Date"])
    data = data.sort_values(by="Date")
    data = data.dropna()
    return data