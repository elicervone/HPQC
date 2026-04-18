import pandas as pd
import matplotlib.pyplot as plt

kernel = pd.read_csv("nsys_kernels_media.csv")
mem = pd.read_csv("nsys_memory_mean.csv")

def plot(x, y, label):
    plt.figure()
    plt.plot(x, y, marker="o")
    plt.xlabel("Distanza")
    plt.ylabel(label)
    plt.title(f"{label} - Distanza")
    plt.grid(True)
    plt.savefig(f"grafico_nsys_{label}.png")


metriche_kernel = kernel.columns[2:]
for kernel_name, gruppo in kernel.groupby("Name"):
    gruppo = gruppo.sort_values("d")

    name = kernel_name.split('::')[1].split('(')[0]  # prendi solo il nome del kernel senza i parametri

    if '<' in name:
        name = name.split('<')[0]  # rimuovi eventuali template parameters

    for metrica in metriche_kernel:
        plot(gruppo["d"], gruppo[metrica], f"{name}_{metrica}")


metriche_mem = mem.columns[2:]
for mem_op, gruppo in mem.groupby("Operation"):
    gruppo = gruppo.sort_values("d")

    name = mem_op.replace("[", "")
    name = name.replace("]", "")

    for metrica in metriche_mem:
        plot(gruppo["d"], gruppo[metrica], f"{name}_{metrica}")
