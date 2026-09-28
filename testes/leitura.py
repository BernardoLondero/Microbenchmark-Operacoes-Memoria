import time

bloco = bytearray(10)

t4 = time.perf_counter_ns()
soma = sum(bloco)
t5 = time.perf_counter_ns()

read_ms = (t5 - t4) / 1_000_000

print("Soma calculada:", soma)
print(f"Tempo de leitura: {read_ms:.6f} ms")