#include <stdio.h>
#include <custatevec.h>    // cuStateVec
#include <cutensornet.h>   // TensorNet

int main() {
    printf("=== Test cuQuantum C/C++ ===\n");

    // Test cuStateVec
    custatevecHandle_t handle;
    if (custatevecCreate(&handle) == CUSTATEVEC_STATUS_SUCCESS) {
        printf("cuStateVec handle creato correttamente!\n");
        custatevecDestroy(handle);
    } else {
        printf("Errore nella creazione handle cuStateVec\n");
    }

    // Test TensorNet
    cutensornetHandle_t tn_handle;
    if (cutensornetCreate(&tn_handle) == CUTENSORNET_STATUS_SUCCESS) {
        printf("TensorNet handle creato correttamente!\n");
        cutensornetDestroy(tn_handle);
    } else {
        printf("Errore nella creazione handle TensorNet\n");
    }

    return 0;
}