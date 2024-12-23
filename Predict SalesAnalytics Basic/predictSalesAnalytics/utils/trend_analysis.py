import matplotlib.pyplot as plt


def plot_historical_trends(data, output_path="output/trend_visualization/trends.png"):
    plt.figure(figsize=(10, 6))
    plt.plot(data["Date"], data["Sales"], label="Historical Sales", color="blue")
    plt.xlabel("Date")
    plt.ylabel("Sales")
    plt.title("Historical Sales Trends")
    plt.legend()
    plt.savefig(output_path)
    plt.close()
