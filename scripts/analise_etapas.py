import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Leitura do arquivo validado
arquivo = 'logs/logs_combinados.csv'

try:
    df = pd.read_csv(arquivo)
    print("Arquivo carregado com sucesso!\n")
except FileNotFoundError:
    print(f"Erro: O arquivo {arquivo} não foi encontrado.")
    exit()

# 2. Definição das variáveis a serem analisadas
operacoes = ['alloc_ms', 'write_ms', 'read_ms', 'free_ms']
titulos = ['Tempo de Alocação', 'Tempo de Escrita', 'Tempo de Leitura', 'Tempo de Liberação']

# 3. Análise Estatística (Média e Desvio Padrão)
# Calcula a média e o desvio padrão dos tempos, para cada sistema, operação e tamanho de bloco
print("--- Tabela de Resultados (Média e Desvio Padrão) ---")
tabela_estatisticas = df.groupby(['sistema', 'bloco_MB'])[operacoes].agg(['mean', 'std'])
print(tabela_estatisticas)
print("\n" + "="*50 + "\n")

# 4. Diferença Matemática entre os Sistemas
# Calcula a diferença entre Windows e Linux para o mesmo tamanho de bloco
print("--- Diferença de Tempo (Média Linux - Média Windows) ---")
medias = df.groupby(['sistema', 'bloco_MB'])[operacoes].mean().reset_index()

# Isola os dados de cada sistema
df_win = medias[medias['sistema'] == 'Windows'].set_index('bloco_MB')[operacoes]
df_lin = medias[medias['sistema'] == 'Linux'].set_index('bloco_MB')[operacoes]

# Calcula a diferença (Valores positivos = Linux demorou mais; Valores negativos = Windows demorou mais)
diferenca = df_lin - df_win
print(diferenca)
print("\n" + "="*50 + "\n")

# 5. Representação Visual (Um gráfico por operação)
sns.set_theme(style="whitegrid")
fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle('Análise Comparativa de Desempenho de Memória', fontsize=16)

# Iterar para gerar cada um dos 4 gráficos
for ax, op, titulo in zip(axes.flatten(), operacoes, titulos):
    
    sns.lineplot(
        data=df, 
        x='bloco_MB', 
        y=op, 
        hue='sistema', 
        marker='o', 
        errorbar='sd', 
        ax=ax
    )
    ax.set_title(titulo, fontsize=14)
    ax.set_xlabel('Tamanho do Bloco (MB)', fontsize=12)
    ax.set_ylabel('Tempo (ms)', fontsize=12)

# Ajuste visual e salvamento da imagem
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.savefig('comparativo_final.png', dpi=600)
print("Gráfico gerado e salvo como 'comparativo_final.png'.")

# Exibir os gráficos na tela
plt.show()