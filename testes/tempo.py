import time

inicio = time.perf_counter_ns()

# operação cujo tempo queremos observar
operacao = 1 + 2

fim = time.perf_counter_ns()

delta_ns = fim - inicio
delta_ms = delta_ns / 1_000_000
delta_s = delta_ms / 1_000

print("Tempo em nanossegundos:", delta_ns)
print(f"Tempo em milissegundos: {delta_ms:.6f} ms")
print(f"Tempo em segundos: {delta_s:.9f} s")
