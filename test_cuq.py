import cuquantum
import cupy as cp

# Test GPU
print("=== Test GPU CuPy ===")
print("Numero di GPU:", cp.cuda.runtime.getDeviceCount())

gpu_name = cp.cuda.runtime.getDeviceProperties(0)['name'].decode('utf-8')
print("Nome GPU:", gpu_name)

x = cp.arange(10)
print("Array test:", x)

#print("Moduli cuQuantum disponibili:", dir(cuquantum))

# Test cuQuantum
print("\n=== Test cuQuantum ===")
print("cuStateVec disponibile:", hasattr(cuquantum, 'custatevec'))
print("cuTensorNet disponibile:", hasattr(cuquantum, 'cutensornet'))
