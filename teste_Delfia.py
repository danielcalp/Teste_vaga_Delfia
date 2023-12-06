import pandas as pd
import configparser

def acessar_formatar_csv(arquivo_csv_origem):
    try:
        # Lê o arquivo CSV diretamente como um DataFrame do Pandas
        df = pd.read_csv(arquivo_csv_origem, delimiter=';')
        return df
    except FileNotFoundError:
        print(f"Erro: Arquivo '{arquivo_csv_origem}' não encontrado.")
        return None
    except pd.errors.EmptyDataError:
        print(f"Erro: Arquivo '{arquivo_csv_origem}' vazio ou formato inválido.")
        return None

def marcar_transacoes_altas(valor_minimo, valor_coluna):
    return 'Alta' if valor_coluna > valor_minimo else 'Normal'

def main():
    # Leitura de parâmetros do arquivo config.cfg
    config = configparser.ConfigParser()
    config.read('config.cfg')

    arquivo_csv_origem = config.get('Valores', 'arquivo_csv_origem')
    df = acessar_formatar_csv(arquivo_csv_origem)

    valor_minimo_transacao = config.getint('Valores', 'limite_transacao')
    if df is not None:
        # Adiciona uma coluna 'Status' indicando se a transação é alta ou não
        
        df['Status'] = [marcar_transacoes_altas(valor_minimo_transacao, valor)
                        for valor in df['Valor da Transação']]
        
        transacoes_altas = df[df['Status'] == 'Alta']

        arquivo_csv_destino = config.get('Valores', 'arquivo_csv_destino')
        transacoes_altas.to_csv(arquivo_csv_destino, index=False, encoding='utf-8-sig', sep=';')
        print("Transações altas salvas em 'transacoes_altas.csv'.")

if __name__ == "__main__":
    main()