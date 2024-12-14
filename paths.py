from pathlib import Path
import os

def create_folder(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

def get_file_path_sl_codes(file_name, file_extension):
    return sl_codes_folder_path.joinpath(file_name + file_extension)

def get_export_folder_path(report_name, report_year, report_month):
    export_folder = sl_codes_folder_path.joinpath('export')
    report_folder = export_folder.joinpath(report_name)
    year_report_folder = report_folder.joinpath(report_year)
    month_report_folder = year_report_folder.joinpath(report_month)
    return month_report_folder

script_path = Path(__file__).resolve()

logistic_utilities_path = script_path.parent

sl_codes_folder_path = logistic_utilities_path.parent

site_workbook_path = sl_codes_folder_path.joinpath('site.xlsx')