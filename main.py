import reader_mgt as mgt
import paths

mgt_config = True
ecs_config = False
nfe_config = False

if mgt_config:

    xml_file_name = '08-agosto - Copia (2)'
    mgt_xml_path = paths.get_file_path_sl_codes(xml_file_name, '.xml')
    
    mgt_export_folder = paths.get_export_folder_path('mgt', '2024', '08')
    paths.create_folder(mgt_export_folder)
    mgt_export_path = mgt_export_folder.joinpath(xml_file_name + '.xlsx')

    mgt.mgt_reader(
        xml_path=mgt_xml_path,
        workbook_path=paths.site_workbook_path,
        wb_sheet_name='mgt',
        export_path=mgt_export_path,
    )

if ecs_config:
    pass

if nfe_config:
    pass

