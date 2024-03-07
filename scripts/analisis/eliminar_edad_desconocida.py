def remove_unknown_age_passengers(df):
    if df is not None:
        df = df.dropna(subset=['Age'])
        return df