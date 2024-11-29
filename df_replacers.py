import pandas as pd

company_list = {
    '01388808000150': 'BERG',
    '19041107000106': 'CEM',
    '36442180000109': 'EN',
    '43706834000120': 'MDC',
    '40119369000132': 'R DE LIMA',
    '43706847000107': 'TF',
    '32253966000127': 'VDCJ',
    '16976734000140': 'RFNS',
    'free': 'R DE LIMA'
}

carrier_list ={
    'J & T BRASIL': 'J&T',
    'Azul': 'AZUL',
    'Correios': 'CORREIOS',
    'Total Express': 'TOTAL',
    'Entrega Expressa - Salvador': 'J&T',
    'Entrega Expressa - Feira de Santana': 'RENILDO',
    'Loja Centro Feira de Santana, 809': 'RETIRADA 809',
    'Loja Salvador': 'RETIRADA PITUBA',
    'Loja Unidade Federação': 'RETIRADA FEDERAÇÃO',
    'Loja Getúlio Vargas 2414': 'RETIRADA 2414',
    'Loja Feira de Santana': 'RETIRADA CAMPO LIMPO'
}

def df_value_replacer(column, rep_dict):
    if pd.isna(column):
        return column
    column = str(column)
    for key, value in rep_dict.items():
        if key in column:
            return value
    return column