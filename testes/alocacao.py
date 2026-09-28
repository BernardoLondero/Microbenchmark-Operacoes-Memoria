import time

tamanho = 2056  # bytes; tamanho do bloco

t0 = time.perf_counter_ns()
bloco = bytearray(tamanho)
t1 = time.perf_counter_ns()

alloc_ms = (t1 - t0) / 1_000_000

print("Quantidade de bytes:", len(bloco))
print(f"Tempo de alocação: {alloc_ms:.6f} ms")
print(list(bloco))