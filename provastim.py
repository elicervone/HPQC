import stim
import cProfile, pstats, io
from pstats import SortKey
import time

p = 0.001
num_shots = 100000

d = 15
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

# Esegui gli shot sulla CPU
start = time.perf_counter()
samples = sampler.sample(num_shots)
end = time.perf_counter()
print("Tempo impiegato:", end - start, "secondi")
#print(samples.shape)
#print(samples[:5])
