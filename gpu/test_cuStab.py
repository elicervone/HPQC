# Se nel terminale scrivo time python test_cuStab.py, posso vedere quanto tempo impiega a eseguire il codice. 
# - real: tempo totale trascorso
# - user: tempo di CPU utilizzato dal processo totale su tutti i core (tempo effettivo di esecuzione del codice)
# - sys: tempo di CPU utilizzato dal sistema operativo per eseguire operazioni a nome del processo (ad esempio, operazioni di I/O)

import stim
import cuquantum.stabilizer as cust
import time
import torch  # solo per sincronizzare la GPU

num_shots = 100000
#print(f"Simulando {num_shots} esecuzioni del circuito...")

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

start = torch.cuda.Event(enable_timing=True)
end = torch.cuda.Event(enable_timing=True)

start.record()
sim.apply(circ)
end.record()

end.synchronize()

print("Tempo:", start.elapsed_time(end) / 1000, "secondi")

# Stampiamo le prime 5 righe della tabella di Pauli.
# L'informazione che viene stampata è la seguente:
# - ogni riga rappresenta i qubit di un frame (un'istanza di esecuzione del circuito)
# - . -> indica che il qubit è in uno stato di identità (non è stato applicato alcun operatore di Pauli)
# - X, Y, Z -> indicano che il qubit è stato colpito da un errore di tipo X, Y o Z rispettivamente

'''pauli_table = sim.get_pauli_table()
num_frames_print = 5
for i in range(num_frames_print):
    print(pauli_table[i])'''