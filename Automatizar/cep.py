import requests
import csv

# Lê o arquivo com os ceps
with open('ceps2.txt', 'r') as input_file:
    ceps = input_file.read().splitlines()

with open ('end3.csv', 'a', newline = '') as output_file:
    writer = csv.writer(output_file)

    # Escreve o cabeçalho do CSV
    writer.writerow(['CEP', 'UF', 'Cidade', 'Bairro'])

for cep in ceps:
    # Remove caracteres especiais 
    cep = cep.replace("-", "").replace(".", "").replace(" ", "")

    if len(cep) == 8:
        link = f'https://viacep.com.br/ws/{cep}/json/'

        requisicao = requests.get(link)
    try:
        if requisicao.status_code == 200:
            dic_requisicao = requisicao.json()

            uf = dic_requisicao['uf']
            cidade = dic_requisicao['localidade']
            bairro = dic_requisicao['bairro']

            # print(f"CEP {cep} encontrado:")
            # print(f"UF: {uf}")
            # print(f"Cidade: {cidade}")
            # print(f"Bairro: {bairro}")
            writer.writerow([cep, uf, cidade, bairro])
    except:
            pass
