import cupy as cp
import numpy as np
from cuquantum import custatevec as csv
from cuquantum import custabilizer as stab

print("=== Test GPU CuPy ===")
print("Numero di GPU:", cp.cuda.runtime.getDeviceCount())
gpu_name = cp.cuda.runtime.getDeviceProperties(0)['name'].decode('utf-8')
print("Nome GPU:", gpu_name)

# ===========================
# Test cuStateVec
# ===========================
print("\n=== Test cuStateVec ===")
n_qubits = 3
dim = 2**n_qubits

# Stato iniziale |000>
state = cp.zeros(dim, dtype=cp.complex128)
state[0] = 1.0

# Creiamo un handle cuStateVec
handle = csv.create()

# Costanti aggiornate per il tipo di calcolo
compute_type = csv.CUDA_COMPUTE_64F

# Applichiamo Hadamard sul qubit 0
H = np.array([[1, 1], [1, -1]], dtype=np.complex128) / np.sqrt(2)
csv.apply_matrix(handle, state, n_qubits, H, qubits=[0], compute_type=compute_type)

# Applichiamo CNOT dal qubit 0 al qubit 1
csv.apply_cnot(handle, state, n_qubits, control=0, target=1, compute_type=compute_type)

# Stampa dello stato
print("Stato cuStateVec:", state.get())

csv.destroy(handle)

# ===========================
# Test cuStabilizer
# ===========================
print("\n=== Test cuStabilizer ===")
n_qubits = 3

# Crea handle
handle = stab.create()

# Crea stato |000>
state = stab.create_state(handle, n_qubits)

# Applica Hadamard sul qubit 0
stab.apply_hadamard(handle, state, 0)

# Applica CNOT 0->1
stab.apply_cnot(handle, state, 0, 1)

# Applica X sul qubit 2
stab.apply_pauli_x(handle, state, 2)

# Misura tutti i qubit
results = stab.measure(handle, state, n_qubits)
print("Risultati misurazione cuStabilizer:", results)

# Pulizia
stab.destroy_state(handle, state)
stab.destroy(handle)
