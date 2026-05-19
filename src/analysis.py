def peak_hour_analysis(df):
    return df.groupby('hour')['delivery_duration'].mean().reset_index()

def demand_by_city(df):
    return df.groupby('city')['order_id'].count().reset_index(name='total_orders')

# 🔥 KPI METRICS (VERY IMPORTANT)
def kpi_metrics(df):
    return {
        "avg_delivery_time": df['delivery_duration'].mean(),
        "peak_delivery_time": df[df['is_peak_hour'] == 1]['delivery_duration'].mean(),
        "non_peak_delivery_time": df[df['is_peak_hour'] == 0]['delivery_duration'].mean(),
        "total_orders": len(df)
    }

# 🔥 ROOT CAUSE ANALYSIS
def root_cause_analysis(df):
    return df.groupby('is_peak_hour')[['delivery_duration', 'distance_km']].mean()