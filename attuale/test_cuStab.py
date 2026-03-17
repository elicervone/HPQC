import stim
import cuquantum.stabilizer as cust
import time
import torch  # solo per sincronizzare la GPU
import sys

num_shots = 100000

p = 0.001
d = int(sys.argv[1])
circ_stim = stim.Circuit.generated(
    "surface_code:rotated_memory_z",
    distance=d,
    rounds=d,
    after_clifford_depolarization=p,
    after_reset_flip_probability=p,
    before_measure_flip_probability=p,
    before_round_data_depolarization=p,
)

circ = cust.Circuit(circ_stim)
sim = cust.FrameSimulator(
    circ_stim.num_qubits,
    num_shots,
    circ_stim.num_measurements,
    num_detectors=circ_stim.num_detectors,
)

start = torch.cuda.Event(enable_timing=True)
end = torch.cuda.Event(enable_timing=True)

start.record()
sim.apply(circ)
end.record()

end.synchronize()

#print("Tempo d=", d, " sh:", num_shots, ":", start.elapsed_time(end) / 1000, "secondi")
print(start.elapsed_time(end) / 1000)