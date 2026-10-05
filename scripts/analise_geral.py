import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Leitura do arquivo unificado
arquivo = 'logs/logs_combinados.csv'

try:
    df = pd.read_csv(arquivo)
    print("Arquivo carregado com sucesso!\n")
except FileNotFoundError:
    print(f"Erro: O arquivo {arquivo} não foi encontrado.")
    exit()

# 2. Criar a coluna de Tempo Total
# Soma os tempos das 4 operações para cada linha (cada teste)
df['tempo_total_ms'] = df['alloc_ms'] + df['write_ms'] + df['read_ms'] + df['free_ms']

# 3. Análise Estatística (Média e Desvio Padrão do Tempo Total)
print("--- Tabela de Resultados: Tempo Total (Média e Desvio Padrão) ---")
tabela_total = df.groupby(['sistema', 'bloco_MB'])['tempo_total_ms'].agg(['mean', 'std'])
print(tabela_total)
print("\n" + "="*50 + "\n")

# 4. Representação Visual (Gráfico do Tempo Total)
sns.set_theme(style="whitegrid")
plt.figure(figsize=(10, 6))

# Gera o gráfico de linha evidenciando a média e a área de desvio padrão
sns.lineplot(
    data=df, 
    x='bloco_MB', 
    y='tempo_total_ms', 
    hue='sistema', 
    marker='o', 
    errorbar='sd' # Mantém a exibição da variação (outliers) no gráfico
)

# Customização de títulos e eixos
plt.title('Comparativo Geral: Tempo Total do Ciclo de Memória', fontsize=16)
plt.xlabel('Tamanho do Bloco (MB)', fontsize=12)
plt.ylabel('Tempo Total (ms)', fontsize=12)
plt.legend(title='Sistema Operacional')

# Ajuste visual e salvamento da imagem
plt.tight_layout()
plt.savefig('comparativo_tempo_total.png', dpi=300)
print("Gráfico gerado e salvo como 'comparativo_tempo_total.png'.")

# Exibir o gráfico na tela
plt.show()