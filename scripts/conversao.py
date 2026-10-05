import pandas as pd
import os

def processar_csv(caminho_arquivo, nome_so):
    """
    Lê o arquivo CSV, converte tipos de dados e realiza validações básicas.
    """
    print(f"\n--- Iniciando o processamento do arquivo: {caminho_arquivo} ({nome_so}) ---")

    # Passo 1: Verificar se o arquivo existe
    if not os.path.exists(caminho_arquivo):
        print(f"ERRO: Arquivo '{caminho_arquivo}' não encontrado.")
        return None

    try:
        # Passo 2: Leitura do arquivo
        # O pandas geralmente tenta inferir os tipos, mas vamos forçar a verificação depois.
        df = pd.read_csv(caminho_arquivo)
        print("Leitura concluída com sucesso.")

        # Passo 3: Adicionar a coluna de identificação do SO
        df['sistema'] = nome_so
        
        # --- VALIDAÇÕES DE CABEÇALHO ---
        colunas_esperadas = ['bloco_MB', 'teste', 'alloc_ms', 'write_ms', 'read_ms', 'free_ms', 'sistema']
        # Verifica se as colunas originais do arquivo estão corretas antes de adicionar 'sistema'
        colunas_originais_esperadas = ['bloco_MB', 'teste', 'alloc_ms', 'write_ms', 'read_ms', 'free_ms']
        
        if list(df.columns)[:-1] != colunas_originais_esperadas:
             print(f"AVISO: Cabeçalho incorreto. Encontrado: {list(df.columns)[:-1]}, Esperado: {colunas_originais_esperadas}")
             return None # Interrompe se o cabeçalho estiver errado

        # --- CONVERSÃO DE TIPOS ---
        print("Convertendo e verificando tipos de dados...")
        try:
             # Garantir que bloco_MB e teste sejam inteiros
             df['bloco_MB'] = df['bloco_MB'].astype(int)
             df['teste'] = df['teste'].astype(int)
             
             # Garantir que os tempos sejam numéricos (float)
             colunas_tempo = ['alloc_ms', 'write_ms', 'read_ms', 'free_ms']
             for col in colunas_tempo:
                 df[col] = pd.to_numeric(df[col], errors='coerce') # errors='coerce' transforma erros em NaN

                 
        except ValueError as e:
            print(f"ERRO DE TIPO: Não foi possível converter os dados. Detalhe: {e}")
            return None

        # --- VALIDAÇÕES DOS DADOS ---
        erros_validacao = 0

        # Verifica se há valores nulos (NaN gerados pelo errors='coerce' ou células vazias originais)
        if df.isnull().values.any():
            print("ERRO DE VALIDAÇÃO: Encontrados valores nulos ou inválidos nas colunas de tempo.")
            print(df[df.isnull().any(axis=1)])
            erros_validacao += 1

        # Verifica quantidade de registros
        qtd_registros = len(df)
        if qtd_registros != 1000:
            print(f"ERRO DE VALIDAÇÃO: Quantidade de registros incorreta. Encontrado: {qtd_registros}, Esperado: 1000.")
            erros_validacao += 1
            
        # Verifica duplicidades
        duplicatas = df[df.duplicated(subset=['bloco_MB', 'teste'], keep=False)]
        if not duplicatas.empty:
             print("ERRO DE VALIDAÇÃO: Encontradas duplicidades de bloco e teste.")
             print(duplicatas)
             erros_validacao += 1

        # Verifica tempos negativos
        for col in colunas_tempo:
            if (df[col] < 0).any():
                print(f"ERRO DE VALIDAÇÃO: Tempos negativos encontrados na coluna {col}.")
                erros_validacao += 1

        if erros_validacao == 0:
            print(f"Processamento e validações do {nome_so} concluídos sem erros.")
            return df
        else:
            print(f"Processamento abortado para {nome_so} devido a erros de validação.")
            return None

    except Exception as e:
        print(f"Erro inesperado ao processar o arquivo: {e}")
        return None


# --- FLUXO PRINCIPAL ---
# Substitua pelos nomes reais dos seus arquivos
arquivo_windows = 'logs/logs_windows.csv'
arquivo_linux = 'logs/logs_linux.csv'

# Processa e valida cada arquivo individualmente
df_win = processar_csv(arquivo_windows, 'Windows')
df_lin = processar_csv(arquivo_linux, 'Linux')



# Se ambos os arquivos passaram na validação, vamos combiná-los
if df_win is not None and df_lin is not None:
    print("\n--- Combinando os dados ---")
    df_completo = pd.concat([df_win, df_lin], ignore_index=True)
    
    # Salvar o resultado final em um novo arquivo
    arquivo_saida = 'logs/logs_combinados.csv'
    df_completo.to_csv(arquivo_saida, index=False)
    print(f"Dados unificados salvos com sucesso em: '{arquivo_saida}'")
    
    # Demonstração de que os dados estão prontos
    print("\nAmostra dos dados processados:")
    print(df_completo.head())
    print("\nInformações do DataFrame unificado:")
    print(df_completo.info())
else:
    print("\nFalha na validação de um ou ambos os arquivos. A combinação não foi realizada.")
    print("Corrija os erros apontados antes de prosseguir.")