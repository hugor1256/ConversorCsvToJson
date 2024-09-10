import json
import os

def ler_dados_csv(arquivo_csv):
    dados_organizados = []

    with open(arquivo_csv, mode='r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            valores = linha.strip().split(';')

            registro = {f"A{i+1}": valor.strip() for i, valor in enumerate(valores) if valor}
            dados_organizados.append(registro)

    return dados_organizados

def salvar_dados_json(dados_organizados, caminho_arquivo):
    with open(caminho_arquivo, mode='w', encoding='utf-8') as arquivo_json:
        json.dump(dados_organizados, arquivo_json, indent=4, ensure_ascii=False)
    print(f"Dados salvos em {caminho_arquivo}")

def buscar_registro(caminho_arquivo, campo, valor):
    if os.path.exists(caminho_arquivo):
        with open(caminho_arquivo, mode='r', encoding='utf-8') as arquivo_json:
            registros = json.load(arquivo_json)
            resultados = [registro for registro in registros if registro.get(campo) == valor]
            return resultados
    else:
        print(f"Arquivo '{caminho_arquivo}' não encontrado.")
        return []

arquivo_csv = 'dados.csv'
caminho_arquivo_json = 'dados.json'

dados_organizados = ler_dados_csv(arquivo_csv)

salvar_dados_json(dados_organizados, caminho_arquivo_json)