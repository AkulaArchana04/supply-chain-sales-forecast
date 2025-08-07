from prophet import Prophet
import pandas as pd
from prepare_data import load_data 

def train_prophet(store_id=1,dept_id=1):
  df=load_data()
  df = df[(df["Store"]==store_id) & (df["Dept"]==dept_id)]

  propft_df = df[["Date", "Weekly_Sales"]].rename(columns={"Date": "ds", "Weekly_Sales": "y"})

  model=Prophet()
  model.fit(propft_df)

  future=model.make_future_dataframe(periods=90)
  future=model.predict(future)

  return future[["ds","yhat","yhat_lower","yhat_upper"]].tail(10)