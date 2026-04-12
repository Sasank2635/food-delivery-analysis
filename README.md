# 🚀 Food Delivery Analytics & Demand Optimization

## 📌 Overview

Built an end-to-end analytics pipeline to analyze food delivery performance, identify demand patterns, and optimize operational efficiency using Python, SQL, and data visualization.

This project simulates real-world business problems faced by platforms like Swiggy, focusing on delivery delays, peak-hour demand, and resource allocation.

---

## 🧠 Problem Statement

Food delivery platforms face challenges such as:

* Increased delivery times during peak hours
* Inefficient allocation of delivery partners
* Lack of visibility into demand patterns

👉 Goal: Use data to **identify bottlenecks and improve delivery performance**

---

## 🛠️ Tech Stack

* **Python** : Pandas, Matplotlib, Scikit-learn
* **SQL** : KPI analysis, demand segmentation, SLA tracking
* **Excel / Power BI (Ready)** : Dashboard visualization
* **Git** : Version control

---

## ⚙️ Project Architecture

```
data → preprocessing → analysis → SQL → ML → visualization → dashboard
```

---

## 📊 Key Features

### ✅ Data Processing

* Cleaned and transformed raw delivery data
* Engineered features like `hour`, `is_peak_hour`

### 📈 Analytics & Insights

* Peak hour analysis (7–10 PM demand spike)
* City-level demand distribution
* Distance vs delivery time impact
* Root cause analysis for delays

### 🗄️ SQL Analytics

* Delivery performance by hour
* Peak vs non-peak comparison
* SLA breach analysis
* Demand distribution (%)

### 🤖 Machine Learning

* Built regression model to predict delivery time
* Evaluated using MAE and R² metrics

### 📊 Visualization

* Delivery time trends across hours
* City-wise order distribution

---

## 📈 Key Insights

* ⏱️ **Peak hours increase delivery time by ~30–40%**
* 📦 High order volume strongly correlates with delays
* 📍 Distance significantly impacts delivery duration
* ⚠️ Identified potential SLA breaches during high-demand periods

---

## 🧪 Experiment Design (A/B Testing)

Proposed experiment to optimize delivery efficiency:

* **Control Group** : Normal delivery partner allocation
* **Test Group** : Increased partners during peak hours
* **Metrics Tracked** :
* Average delivery time
* Order completion rate

---

## 📊 Dashboard

### Key Metrics Tracked:

* Average Delivery Time
* Total Orders
* Peak vs Non-Peak Performance

📸 Dashboard Preview:

![Dashboard](https://chatgpt.com/dashboard/dashboard_screenshot.png)

---

## 📁 Outputs

### Visualizations

* `outputs/peak_hour_trend.png`
* `outputs/city_demand.png`

### Dashboard Data

* `dashboard/peak_hour_data.csv`
* `dashboard/city_data.csv`
* `dashboard/kpi_metrics.json`

---

## ▶️ How to Run

```bash
# Install dependencies
pip install -r requirements.txt

# Run pipeline
cd src
python run_analysis.py
```

---

## 📌 Business Impact

This project demonstrates how data can:

* Improve delivery efficiency
* Reduce customer wait times
* Optimize resource allocation
* Support data-driven decision-making

---

## 🚀 Future Improvements

* Real-time demand forecasting
* Rider allocation optimization model
* Integration with live APIs
* Interactive dashboard (Streamlit / Power BI)

---

## 👨‍💻 Author

**Sasanka Sekhar Upadhyaya**
📧 [sasanka.sekhar.upadhyaya2002@gmail.com](mailto:sasanka.sekhar.upadhyaya2002@gmail.com)
🔗 GitHub: https://github.com/Sasank2635/food-delivery-analysis.git

---
