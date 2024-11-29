from openpyxl import load_workbook
from openpyxl.styles import Border, Side, NamedStyle, Alignment

black_border = Border(
    top=Side(style='thin'),
    bottom=Side(style='thin'),
    left=Side(style='thin'),
    right=Side(style='thin')
)

date = NamedStyle(
    name='mps_date', 
    number_format="DD/MM/YYYY", 
    )

br_currency = NamedStyle(
    name='mps_br_currency',
    number_format='R$0.00',
)


def styles_verify(styles_list, workbook):
    for style in styles_list:
        if style.name not in workbook.style_names:
            workbook.add_named_style(style)

center_alignment = Alignment(horizontal='center')
