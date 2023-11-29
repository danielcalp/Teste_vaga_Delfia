import csv
import json
import pandas as pd

# Função para acessar e formatar os dados do arquivo CSV
def acessar_formatar_csv(caminho_arquivo):
    dados_formatados = []

    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo_csv:
        # Cria um objeto leitor de dicionário CSV com ponto e vírgula como delimitador
        leitor_csv = csv.DictReader(arquivo_csv, delimiter=';')

        # Itera sobre as linhas do arquivo CSV
        for linha in leitor_csv:
            # Remove o caractere (\ufeff) dos cabeçalhos, se presente
            linha_corrigida = {chave.replace('\ufeff', ''): valor for chave, valor in linha.items()}
            # Adiciona cada linha como um dicionário à lista
            dados_formatados.append(linha_corrigida)

    return dados_formatados

# Caminho do arquivo CSV
caminho_arquivo_csv = 'transacoes.csv'

# Obtém e formata os dados do arquivo CSV
dados_csv_formatados = acessar_formatar_csv(caminho_arquivo_csv)

# Lista para armazenar transações com valores altos
transacoes_altas = []

# Itera sobre as linhas formatadas do CSV
for linha_csv in dados_csv_formatados:
    nome_cliente = linha_csv['Nome do Cliente']
    valor_transacao = linha_csv['Valor da Transação']
    data_transacao = linha_csv['Data da Transação']

    # Verifica se o valor da transação é maior que 1000
    if int(valor_transacao) > 1000:
        transacoes_altas.append(linha_csv)

# Cria um DataFrame do pandas com as transações altas
df_transacoes_altas = pd.DataFrame(transacoes_altas)

# Salva as transações altas em um novo arquivo CSV
df_transacoes_altas.to_csv('transacoes_altas.csv', index=False, encoding='utf-8-sig', sep=';')
