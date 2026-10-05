# Microbenchmark de Operações de Memória: Comparativo Windows vs. Linux

Repositório destinado ao armazenamento de artefatos, códigos-fonte, conjuntos de dados e documentação do experimento comparativo de desempenho de memória RAM entre os sistemas operacionais **Windows** e **Linux**. 

A investigação integra o escopo da disciplina de **Programação para Ciência de Dados** e fornece evidências quantitativas para subsidiar escolhas de infraestrutura de software em camadas de integração de **Cidades Inteligentes**.

---

## 1. Protocolo Experimental e Parâmetros

O experimento foi projetado seguindo um protocolo estrito de pré-registro experimental para assegurar a reprodutibilidade dos resultados. A tabela a seguir especifica cada elemento que compõe o desenho experimental do microbenchmark:

| Elemento do Protocolo | Requisito / Definição |
| :--- | :--- |
| **Sistemas Operacionais** | Windows e Linux |
| **Operações Medidas** | Alocação, Escrita, Leitura e Liberação |
| **Sequência de Execução** | Alocar $\rightarrow$ Escrever $\rightarrow$ Ler $\rightarrow$ Liberar |
| **Faixa de Tamanho de Bloco** | 100 MB a 1.000 MB (passo de 100 MB, totalizando 10 tamanhos) |
| **Número de Repetições** | 100 testes independentes para cada tamanho de bloco |
| **Volume de Amostras** | 1.000 registros por sistema operacional (2.000 registros no total) |
| **Precisão Temporal** | Medição em nanossegundos via `time.perf_counter_ns()`, convertida e salva em milissegundos (`ms`) |
| **Formato de Persistência** | Arquivos CSV com codificação UTF-8 |
| **Esquema do Cabeçalho** | `bloco_MB,teste,alloc_ms,write_ms,read_ms,free_ms` |

### Controle de Equivalência do Ambiente
Para garantir o isolamento da variável independente (Sistema Operacional) e a consistência das variáveis controladas (Hardware e Software):
* **Configuração de Hardware**: Execução em duas Máquinas Virtuais (*VMs*) idênticas no mesmo computador hospedeiro com idêntica atribuição de vCPUs e memória RAM.
* **Ambiente Python**: Mesma versão do interpretador Python (3.14.4) instalada em ambos os sistemas.
* **Isolamento de Processos**: Fechamento de todas as aplicações não essenciais em segundo plano durante as rotinas de amostragem.

---

## 2. Pré-requisitos e Dependências

Para executar os scripts de coleta, processamento e análise, são necessários a linguagem Python e as bibliotecas especializadas para ciência de dados. As dependências podem ser instaladas diretamente via gerenciador de pacotes `pip`:

```bash
pip install pandas matplotlib seaborn
```

---

## 3. Guia de Reprodução Passo a Passo

A reprodução do experimento é realizada em três etapas sequenciais: amostragem, validação/unificação dos logs e geração da análise estatística.

```bash
python scripts/medicao_geral.py
```

```bash
python scripts/processamento_csv.py
```

```bash
python scripts/analise_etapas.py
python scripts/analise_geral.py
```

---

## 4. Equipe e Integrantes

Este projeto foi desenvolvido colaborativamente por:
* [Bernardo Londero](https://github.com/BernardoLondero)
* [Gabriel Boelter Cervi](https://github.com/gabrielbcervi)
* [Gustavo Baptista](https://github.com/SakamotoGB)
