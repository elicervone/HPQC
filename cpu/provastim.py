import stim
import time
import gc
import sys

p = 0.001
num_shots = 100000

# prende in input dallo script chiamante la distanza del codice da testare
d = int(sys.argv[1])

circ = stim.Circuit.generated(
    "surface_code:rotated_memory_z",
    distance=d,
    rounds=d,
    after_clifford_depolarization=p,
    after_reset_flip_probability=p,
    before_measure_flip_probability=p,
    before_round_data_depolarization=p,
)

# Crea un sampler CPU
sampler = circ.compile_sampler()

# Esegue gli shot sulla CPU
start = time.perf_counter()
samples = sampler.sample(num_shots)
end = time.perf_counter()

#with open(f"tempi_{d}.txt", "a") as f:
#    f.write(f"Tempo impiegato: {end - start} secondi\n")
    #print(f"Shot rate: {num_shots/(end-start):.2e} shots/sec")

#print(f"Tempo impiegato: {end - start} secondi")
print(end-start)

# Dealloca esplicitamente gli oggetti grandi
del circ
del sampler
del samples
gc.collect()  # forza il garbage collector