import csv
import time

# definir tamanho do bloco em MB
tamanho_MB = 1

# passando para bytes
tamanho = tamanho_MB * 1_000_000

print(f"Tamanho do Bloco: {tamanho_MB} MBs \n")
logs = []

for i in range(1, 101):
    # ALOCACAO
    t0 = time.perf_counter_ns()
    bloco = bytearray(tamanho)
    t1 = time.perf_counter_ns()

    alocacao_ns = (t1 - t0)





    # ESCRITA
    #padrao de dados que serão escritos
    padrao = b'\xAA' * tamanho

    t2 = time.perf_counter_ns()
    bloco[:] = padrao
    t3 = time.perf_counter_ns()

    escrita_ns = (t3 - t2)

    


    # LEITURA
    t4 = time.perf_counter_ns()
    soma = sum(bloco)
    t5 = time.perf_counter_ns()

    leitura_ns = (t5 - t4)





    # LIBERACAO
    t6 = time.perf_counter_ns()
    bloco.clear()
    del bloco
    t7 = time.perf_counter_ns()

    liberacao_ns = (t7 - t6)


    log = [
        i,
        tamanho_MB,
        alocacao_ns,
        escrita_ns,
        leitura_ns,
        liberacao_ns
    ]

    logs.append(log)

#print(f"Tempo liberacao: {liberacao_ns} ns")
#print(f"Tempo de leitura: {leitura_ns} ns \n")
#print(f"Tempo de escrita: {escrita_ns} ns \n")
#print(f"Tempo Alocacao: {alocacao_ns} ns \n")

with open('logs.csv', 'w', newline='') as arquivo_csv:
    escritor = csv.writer(arquivo_csv)
    escritor.writerow(['Iteracao', 'Tamanho (MB)', 'Alocacao (ns)', 'Escrita (ns)', 'Leitura (ns)', 'Liberacao (ns)'])
    for log in logs:
        escritor.writerow(log)
print(logs)