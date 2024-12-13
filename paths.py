from pathlib import Path

script_path = Path(__file__).resolve()

logistic_utilities_path = script_path.parent

sl_codes_path = logistic_utilities_path.parent

ecs_path = sl_codes_path.joinpath('ecs.csv')
mgt_path = sl_codes_path.joinpath('mgt.xml')
site_workbook_path = sl_codes_path.joinpath('site.xlsx')