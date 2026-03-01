# Se nel terminale scrivo time python test_cuStab.py, posso vedere quanto tempo impiega a eseguire il codice. 
# - real: tempo totale trascorso
# - user: tempo di CPU utilizzato dal processo totale su tutti i core (tempo effettivo di esecuzione del codice)
# - sys: tempo di CPU utilizzato dal sistema operativo per eseguire operazioni a nome del processo (ad esempio, operazioni di I/O)

import stim
import cuquantum.stabilizer as cust

num_shots = 100000

p = 0.001
d = 10
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

sim.apply(circ)