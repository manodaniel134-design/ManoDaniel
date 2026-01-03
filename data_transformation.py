import pandas as pd
from sklearn.preprocessing import StandardScaler

def transform_data(df):
    df = df.copy()

    # Convert date column
    df["Order Date"] = pd.to_datetime(df["Order Date"])
    df["Order Year"] = df["Order Date"].dt.year
    df["Order Month"] = df["Order Date"].dt.month

    # Scale numeric columns (USE REAL COLUMN NAMES)
    scaler = StandardScaler()
    df[["Quantity", "Unit Price", "Sales"]] = scaler.fit_transform(
        df[["Quantity", "Unit Price", "Sales"]]
    )

    return df
