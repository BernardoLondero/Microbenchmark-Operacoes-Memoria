import time

# definir tamanho do bloco em MB
tamanho_MB = 1

# passando para bytes
tamanho = tamanho_MB * 1024 * 1024

print(f"Tamanho do Bloco: {tamanho_MB} MBs \n")

# ALOCACAO
t0 = time.perf_counter_ns()
bloco = bytearray(tamanho)
t1 = time.perf_counter_ns()

alocacao_ns = (t1 - t0)

print(f"Tempo Alocacao: {alocacao_ns} ns \n")



# ESCRITA
#padrao de dados que seram escritos
padrao = b'\xAA' * tamanho

t2 = time.perf_counter_ns()
bloco[:] = padrao
t3 = time.perf_counter_ns()

escrita_ns = (t3 - t2)

print(f"Tempo de escrita: {escrita_ns} ns \n")



# LEITURA
t4 = time.perf_counter_ns()
soma = sum(bloco)
t5 = time.perf_counter_ns()

leitura_ns = (t5 - t4)

print(f"Tempo de leitura: {leitura_ns} ns \n")



# LIBERACAO
t6 = time.perf_counter_ns()
bloco.clear()
del bloco
t7 = time.perf_counter_ns()

liberacao_ns = (t7 - t6)

print(f"Tempo liberacao: {liberacao_ns} ns")
