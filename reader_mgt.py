import pandas as pd
import xml.etree.ElementTree as ET
from openpyxl import load_workbook
from openpyxl.styles import Border, Side, NamedStyle, Alignment
import my_person_styles as mps
import cell_formatts as cf
import df_tools as dftools
import my_paths as paths

def magento_reader(magento_xml):
    namespaces = {'ss': 'urn:schemas-microsoft-com:office:spreadsheet'}
    tree = ET.parse(magento_xml)
    root = tree.getroot()
    data_rows = []

    for row in root.findall('.//ss:Worksheet/ss:Table/ss:Row', namespaces):
        row_data = []
        for cell in row.findall('ss:Cell', namespaces):
            data = cell.find('ss:Data', namespaces)
            row_data.append(data.text.strip() if data is not None and data.text else "")
        data_rows.append(row_data)

    data_rows.pop()

    column_names = data_rows[0] if data_rows else []
    df_magento_xml = pd.DataFrame(data_rows[1:], columns=column_names)
    return df_magento_xml

magento_file_name = '08-agosto - Copia (2)'
magento_path = f'C:\\Users\\jonat\\Desktop\\sl_codes\\{magento_file_name}' + '.xml'
df = magento_reader(magento_path)
main_df = pd.read_excel(paths.site_sheet_path, sheet_name='Magento')


new_df = df[[
    'Pedido #', 'Comprado Em', 'Firstname', 'Email', 'Número CPF/CNPJ',
    'Shipping Telephone', 'Frete', 'Desconto', 'Total da Venda',
    'Payment Type', 'Status'
    ]]


magento_float_columns = ['Frete', 'Desconto', 'Total da Venda']
cf.br_currency(new_df, magento_float_columns)

new_df = new_df.rename(columns={'Pedido #': 'OC'})

new_df['Comprado Em'] = new_df['Comprado Em'].apply(cf.date)
new_df['OC'] = pd.to_numeric(new_df['OC'], errors='coerce')

final_df = dftools.update_df(main_df, new_df, on_column='OC')
final_df = final_df.sort_values(by='Comprado Em')

with pd.ExcelWriter(
    paths.site_sheet_path,
    engine='openpyxl',
    mode='a',
    if_sheet_exists='overlay'
    ) as writer:
    final_df.to_excel(writer, sheet_name='Magento', index=False)


# Estilização
site_sheet_path = 'C:\\Users\\jonat\\Desktop\\sl_codes\\site.xlsx'
wb = load_workbook(site_sheet_path)
ws = wb['Magento']
last_row = ws.max_row + 1

# Verificar estilos do WB e adicionar
my_named_styles = [mps.br_currency, mps.date]
mps.styles_verify(my_named_styles, wb)

date_columns = ['B']
currencies_columns = ['G', 'H' , 'I']

for row in ws.iter_rows():
    if any(cell.value is not None for cell in row):
        for cell in row:
            if cell.column_letter in date_columns:
                cell.style = mps.date.name

            if cell.column_letter in currencies_columns:
                cell.style = mps.br_currency.name

            cell.border = mps.black_border
            cell.alignment = mps.center_alignment
            cell.font = "Lexend"


wb.save(site_sheet_path)
            

print('Adição e estilização de dados em site.xlsx "magento" concluída!')

mgt_export_name = f'{magento_file_name} teste'
mgt_export_path = f'C:\\Users\\jonat\\Desktop\\sl_codes\\export{mgt_export_name}' + '.xlsx'
new_df.to_excel(mgt_export_path, index=False)
