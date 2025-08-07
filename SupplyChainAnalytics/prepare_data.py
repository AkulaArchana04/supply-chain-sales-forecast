import pandas as pd

def load_data():
    sales_df=pd.read_csv("train.csv",parse_dates=["Date"])
    feature_df=pd.read_csv("features.csv",parse_dates=["Date"])
    stores_df=pd.read_csv("stores.csv")

    merged=pd.merge(sales_df,feature_df,on=["Store","Date"],how="left")
    merged=pd.merge(merged,stores_df,on="Store",how="left")
    for i in range(1,6):
        merged[f"MarkDown{i}"] = merged[f"MarkDown{i}"].fillna(0) 
      
    return merged


#streamlit run g.py