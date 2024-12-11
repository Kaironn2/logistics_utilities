import pandas as pd

def update_df(df_main, df_new, on_column):
    existing_id = df_main[on_column].isin(df_new[on_column])

    df_updated = pd.merge(
        df_main[~existing_id],
        df_new,
        on=on_column,
        how='outer',
        suffixes=('', '_new')
    )

    for column in df_new.columns:
        if column != on_column:  # Evita sobreposição do ID
            df_updated[column] = df_updated[f'{column}_new'].combine_first(df_updated[column])
            df_updated.drop(columns=[f'{column}_new'], inplace=True)
    
    return df_updated
