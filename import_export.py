import pandas as pd

def import_data(path):
    df = pd.read_csv(path)
    print("First 5 rows:")
    print(df.head())
    print("\nDataset Info:")
    print(df.info())
    return df

def export_data(df, path):
    df.to_csv(path, index=False)
    print(f"Cleaned data exported to {path}")
