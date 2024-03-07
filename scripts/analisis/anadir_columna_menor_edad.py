def add_minor_column(df):
    if df is not None:
        df['Minor'] = df['Age'] < 18
        return df