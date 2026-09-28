import time

bloco_teste = bytearray(10)
padrao = b'\xAA' * len(bloco_teste)  # dez bytes; preparado fora da medição

t2 = time.perf_counter_ns()
bloco_teste[:] = padrao
t3 = time.perf_counter_ns()

write_ms = (t3 - t2) / 1_000_000

print(f"Tempo de escrita: {write_ms:.6f} ms")
print("Tamanho após a escrita:", len(bloco_teste))  # 10