import matplotlib.pyplot as plt

def plot_peak_hours(df):
    plt.figure()
    plt.plot(df['hour'], df['delivery_duration'], marker='o')
    plt.title("Avg Delivery Time by Hour")
    plt.xlabel("Hour")
    plt.ylabel("Delivery Time (mins)")
    plt.grid()
    plt.savefig("../outputs/peak_hour_trend.png")

def plot_city_demand(df):
    plt.figure()
    plt.bar(df['city'], df['total_orders'])
    plt.title("Order Volume by City")
    plt.xlabel("City")
    plt.ylabel("Total Orders")
    plt.savefig("../outputs/city_demand.png")