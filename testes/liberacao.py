import time

bloco = bytearray(10)

t6 = time.perf_counter_ns()
bloco.clear()
del bloco
t7 = time.perf_counter_ns()

free_ms = (t7 - t6) / 1_000_000
print(f"Tempo medido: {free_ms:.6f} ms")
