import csv
import time

# definir tamanho do bloco em MB
lista_tamanhos_MB = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
# lista_tamanhos_MB = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #teste

# definir numero de iteracoes por bloco
iteracoes_bloco = range(1, 101)

logs = []

for i_bloco in lista_tamanhos_MB:
    tamanho = i_bloco * 1024 * 1024

    for i in iteracoes_bloco:
        # ALOCACAO
        t0 = time.perf_counter_ns()
        bloco = bytearray(tamanho)
        t1 = time.perf_counter_ns()

        alocacao_ns = (t1 - t0) / 1_000_000


        # ESCRITA
        #padrao de dados que serão escritos
        padrao = b'\xAA' * tamanho

        t2 = time.perf_counter_ns()
        bloco[:] = padrao
        t3 = time.perf_counter_ns()

        escrita_ns = (t3 - t2) / 1_000_000


        # LEITURA
        t4 = time.perf_counter_ns()
        leitura_em_bloco = bloco[:]
        t5 = time.perf_counter_ns()

        leitura_ns = (t5 - t4) / 1_000_000


        # LIBERACAO
        t6 = time.perf_counter_ns()
        bloco.clear()
        del bloco
        t7 = time.perf_counter_ns()

        liberacao_ns = (t7 - t6) / 1_000_000



        log = [
            i_bloco,
            i,
            alocacao_ns,
            escrita_ns,
            leitura_ns,
            liberacao_ns
        ]

        logs.append(log)
    print(f"Bloco {lista_tamanhos_MB.index(i_bloco)+ 1} OK")

with open('logs.csv', 'w', newline='') as arquivo_csv:
    escritor = csv.writer(arquivo_csv)
    escritor.writerow(["bloco_MB", "teste", "alloc_ms", "write_ms", "read_ms", "free_ms"])
    for log in logs:
        escritor.writerow(log)

print("Medição completa e Arquivada")
