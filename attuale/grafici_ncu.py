import pandas as pd
import matplotlib.pyplot as plt

validate_0 = pd.read_csv("validate_circuit_kernel_0.csv")
validate_1 = pd.read_csv("validate_circuit_kernel_1.csv")
simulazione = pd.read_csv("void circuit_kernel_batch_plain_stack_2.csv")

def grafici_metriche(file):
    plt.figure()

    x = file["Distanza"]

    for col in file.columns[1:]:
        metrica = col.split('.')[0] + '_' + col.split('.')[1]
        if '%' in col:
            metrica = col.split('.')[0] + '_' + col.split('.')[1] + ' [%]'
        plt.plot(x, file[col], marker='o', label=metrica)
        plt.grid(True)
        plt.title(f"grafico_{metrica}")
        plt.xlabel("Distanza")
        plt.ylabel(metrica)
        plt.savefig(f"grafico_ncu_{metrica}_simulazione.png")
        plt.close()

grafici_metriche(simulazione)