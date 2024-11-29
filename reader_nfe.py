import os
import pandas as pd
import xml.etree.ElementTree as ET

_file_name = "2024"

folder_path = f'C:\\Users\\Jonh\\Desktop\\new bd\\3-Nfe\\{_file_name}\\'

data = []
nfe_counter = 0
error_logs = []

def extract_data_from_xml(file_path):
    global nfe_counter

    # Verifica se o arquivo está vazio
    if os.path.getsize(file_path) == 0:
        print(f"O arquivo {file_path} está vazio.")
        error_logs.append(f'{nfe_counter} - Arquivo vazio - {file_path}')
        return None

    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
    except ET.ParseError as e:
        print(f'Erro ao analisar o arquivo {file_path}: {e}')
        error_logs.append(f'{nfe_counter} - Erro de análise - {file_path} -> {e}')
        return None

    nfe_counter += 1

    try:
        namespaces = {'nfe': 'http://www.portalfiscal.inf.br/nfe'}

        xped = root.find('.//nfe:xPed', namespaces)
        cnpj = root.find('.//nfe:CNPJ', namespaces)
        xnome = root.find('.//nfe:xNome', namespaces)
        chnfe = root.find('.//nfe:chNFe', namespaces)
        vfrete_total = root.find('.//nfe:total/nfe:ICMSTot/nfe:vFrete', namespaces)
        vnf = root.find('.//nfe:vNF', namespaces)
        dhrecbto = root.find('.//nfe:dhRecbto', namespaces)
        cpf = root.find('.//nfe:CPF', namespaces)
        vdesc_total = root.find('.//nfe:total/nfe:ICMSTot/nfe:vDesc', namespaces)
        transportadora = root.find('.//nfe:transp/nfe:transporta/nfe:xNome', namespaces)

        # Contagem de produtos que não estão vazias
        produtos = root.findall('.//nfe:det/nfe:prod/nfe:xProd', namespaces)  
        count_produtos = sum(1 for p in produtos if p.text and p.text.strip())
        
        # Diferença frete e nf para obter valor da somatória dos produtos
        vfrete = float(vfrete_total.text) if vfrete_total is not None and vfrete_total.text else 0.0
        vnf_valor = float(vnf.text) if vnf is not None and vnf.text else 0.0
        dif_frete_nf = abs(vfrete - vnf_valor)

        print(f'{nfe_counter} - Arquivo {chnfe.text} lido com sucesso')

        return {
            'nfe:xPed': int(xped.text) if xped is not None else None,
            'nfe:CNPJ': str(cnpj.text) if cnpj is not None else None,
            'nfe:xNome': xnome.text if xnome is not None else None,
            'nfe:chNFe': chnfe.text if chnfe is not None else None,
            'nfe:vFrete': float(vfrete_total.text) if vfrete_total is not None else None,
            'nfe:vNF': float(vnf.text) if vnf is not None else None,
            'nfe:dhRecbto': dhrecbto.text if dhrecbto is not None else None,
            'nfe:CPF': cpf.text if cpf is not None else None,
            'nfe:vProduto': dif_frete_nf,
            'nfe:vDesc': float(vdesc_total.text) if vdesc_total is not None else None,
            'produtos_count': count_produtos,
            'transportadora': transportadora.text if transportadora is not None else None
        }
    except Exception as e:
        print(f"Erro ao processar o arquivo {file_path}: {e}")
        error_logs.append(f'{nfe_counter} - Erro de processamento - {file_path} -> {e}')
        return None

for dirpath, _, filenames in os.walk(folder_path):
    print('Lendo', dirpath)
    for folder_name in filenames:
        if folder_name.lower().endswith('.xml'):
            file_path = os.path.join(dirpath, folder_name)
            extracted_data = extract_data_from_xml(file_path)
            if extracted_data:
                data.append(extracted_data)

df = pd.DataFrame(data)

print(df.head())

df.to_excel(f"Notas Fiscais {_file_name}.xlsx", index=False)
with open(f'{_file_name}.txt', 'w') as file:
    file.write("\n".join(error_logs))

print("Exportação concluída!")
