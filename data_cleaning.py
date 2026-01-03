def clean_data(df):
    df = df.copy()

    # Remove duplicates
    df.drop_duplicates(inplace=True)

    # Handle missing values
    df.fillna(method="ffill", inplace=True)

    return df
