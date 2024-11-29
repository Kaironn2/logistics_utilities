import pandas as pd

def date(column):
    return pd.to_datetime(column[:10], errors='coerce', dayfirst=True)

def br_currency(df, columns):
    for column in columns:
        df[column] = df[column].str.replace('R$', '', regex=False)
        df[column] = df[column].str.replace('.', '', regex=False)
        df[column] = df[column].str.replace(',', '.', regex=False)
        df[column] = df[column].astype(float)
