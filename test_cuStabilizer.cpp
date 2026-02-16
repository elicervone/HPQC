/* Per compilare: nvcc test_cuStabilizer.cpp -o test_cuStabilizer -I ~/miniconda3/include -L ~/miniconda3/lib -lcustabilizer
   Per eseguire: ./test_cuStabilizer
*/

#include <custabilizer.h>
#include <cuda_runtime.h>
#include <cstdlib>   // malloc, free
#include <cstdio>    // printf


int main() {
    // Create library handle
    custabilizerHandle_t handle;
    custabilizerCreate(&handle);

    // Define a simple circuit
    const char* circuitString =
        "X_ERROR(0.5) 0 1\n"    // era 0.1 ma ho cambiato a 0.5 per vedere più risultati diversi per sapere se funzionava
        "H 0\n"
        "CNOT 0 1\n"
        "M 0 1\n";

    // Create circuit
    // Vediamo quanto spazio serve
    int64_t bufferSize;
    custabilizerCircuitSizeFromString(handle, circuitString, &bufferSize);
    // Allochiamo lo spazio necessario sulla GPU
    void* bufferDevice;
    cudaMalloc(&bufferDevice, bufferSize);

    // creazione del circuito
    custabilizerCircuit_t circuit;
    custabilizerCreateCircuitFromString(handle, circuitString, bufferDevice,
                                       bufferSize, &circuit);

    // Set up frame simulator parameters
    int64_t numQubits = 2;
    int64_t numShots = 1017;
    int64_t numMeasurements = 2;
    int64_t stride = ((numShots + 7) / 8 + 3) & ~3;  // Pad to multiple of 4

    // Create frame simulator
    custabilizerFrameSimulator_t frameSimulator;
    custabilizerCreateFrameSimulator(handle, numQubits, numShots,
                                    numMeasurements, stride, &frameSimulator);

    // Allocate and initialize bit tables
    int64_t bitTableBytes = numQubits * stride;
    int64_t mTableBytes = numMeasurements * stride;

    custabilizerBitInt_t* xTableDevice;
    custabilizerBitInt_t* zTableDevice;
    custabilizerBitInt_t* mTableDevice;

    cudaMalloc(&xTableDevice, bitTableBytes);
    cudaMalloc(&zTableDevice, bitTableBytes);
    cudaMalloc(&mTableDevice, mTableBytes);

    // inizializzazione
    cudaMemset(xTableDevice, 0, bitTableBytes);
    cudaMemset(zTableDevice, 0, bitTableBytes);
    cudaMemset(mTableDevice, 0, mTableBytes);

    // Apply circuit to the Pauli frames
    uint64_t seed = 42;
    int randomizeFrameAfterMeasurement = 1;
    cudaStream_t stream = 0;

    custabilizerFrameSimulatorApplyCircuit(handle, frameSimulator, circuit,
                                          randomizeFrameAfterMeasurement, seed,
                                          xTableDevice, zTableDevice, mTableDevice,
                                          stream);

    // aspetta che la GPU finisca
    cudaStreamSynchronize(stream);

    // aggiunto io per vedere i risultati delle misure, non so se è il modo giusto ma almeno vedo se funziona o no
    // Alloca array host per copiare i risultati delle misure
    custabilizerBitInt_t* mTableHost = (custabilizerBitInt_t*) malloc(numMeasurements * stride);

    // Copia da GPU a CPU
    cudaMemcpy(mTableHost, mTableDevice, numMeasurements * stride, cudaMemcpyDeviceToHost);

    // Stampa i primi 10 shot delle misure
    printf("Misure dei primi 10 shots:\n");
    for (int shot = 0; shot < 10 && shot < numShots; shot++) {
        printf("Shot %d: ", shot);
        for (int m = 0; m < numMeasurements; m++) {
            // Ogni misura è un bit: usa la funzione custabilizerBitGetFromTable per estrarlo
            int bit = (mTableHost[m * stride / sizeof(custabilizerBitInt_t) + shot / 64] >> (shot % 64)) & 1;
            printf("%d ", bit);
        }
        printf("\n");
    }
    // Fine aggiunta

    // Clean up
    free(mTableHost);   // aggiunto io per liberare la memoria host
    cudaFree(xTableDevice);
    cudaFree(zTableDevice);
    cudaFree(mTableDevice);
    custabilizerDestroyFrameSimulator(frameSimulator);
    custabilizerDestroyCircuit(circuit);
    cudaFree(bufferDevice);
    custabilizerDestroy(handle);
    return 0;
}
