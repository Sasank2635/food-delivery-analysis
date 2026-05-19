import pathlib
import matplotlib.pyplot as plt

OUTPUTS = pathlib.Path(__file__).resolve().parent.parent / "outputs"


def plot_peak_hours(df) -> None:
    plt.figure()
    plt.plot(df['hour'], df['delivery_duration'], marker='o')
    plt.title("Avg Delivery Time by Hour")
    plt.xlabel("Hour")
    plt.ylabel("Delivery Time (mins)")
    plt.grid()
    plt.savefig(OUTPUTS / "peak_hour_trend.png")
    plt.close()


def plot_city_demand(df) -> None:
    plt.figure()
    plt.bar(df['city'], df['total_orders'])
    plt.title("Order Volume by City")
    plt.xlabel("City")
    plt.ylabel("Total Orders")
    plt.savefig(OUTPUTS / "city_demand.png")
    plt.close()
