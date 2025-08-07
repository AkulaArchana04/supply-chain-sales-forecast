
# 📦 Supply Chain Sales Forecast Dashboard

An interactive web application built using **Streamlit** that visualizes and forecasts weekly sales across different **stores and departments** using **Facebook Prophet**. It also features a dynamic dashboard showing KPIs such as total sales, average weekly sales, and more.

---

## 📊 Features

- 🏪 Filter by Store and Department
- 📉 Visualize Historical Weekly Sales
- 🔮 Forecast next 90 days using Prophet
- 📋 View KPIs like Total Sales & Avg Weekly Sales
- 💡 User-friendly and colorful interface

---

## ⚙️ Technologies Used

| Technology | Purpose |
|-----------|---------|
| `Streamlit` | Web app framework |
| `Prophet` (Facebook) | Time series forecasting |
| `Plotly` | Interactive visualizations |
| `Pandas` | Data manipulation |
| `Python` | Core programming language |

---

## 📁 Project Structure

```
supply-chain-sales-forecast/
│
├── SupplyChainAnalytics/
│   ├── features.csv
│   ├── train.csv
│
├── prepare_data.py
├── forecast_model.py
├── app.py
├── requirements.txt
└── README.md

## 📦 Requirements

Install dependencies using:

pip install -r requirements.txt

Your `requirements.txt` should include:


streamlit
prophet
pandas
plotly

---

## 🚀 How to Run the App

1. **Clone the repository**


git clone https://github.com/AkulaArchana04/supply-chain-sales-forecast.git
cd supply-chain-sales-forecast


2. **Install required libraries**


pip install -r requirements.txt


3. **Run the Streamlit app**


streamlit run app.py

4. Open your browser to:

```
http://localhost:8501
```

---

## 🧠 How it Works (Brief Explanation)

- Loads and filters sales data from `train.csv` using `prepare_data.py`
- Trains a **Prophet forecasting model** on filtered sales
- Displays:
  - A historical **line plot** using Plotly
  - A 90-day **forecast chart** with upper/lower bounds
  - A clean **KPI dashboard** for metrics like total and average weekly sales

---

## 📬 Author

**Archana Akula**
