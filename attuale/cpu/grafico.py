import pandas as pd
import matplotlib.pyplot as plt

def plot(x, y, label, speedup=False):
    plt.figure()
    plt.plot(x, y, marker="o")
    plt.xlabel("Distanza")
    plt.ylabel(label)
    if not speedup:
        plt.title(f"{label} - Distanza")
    else:
        plt.title("Speedup GPU rispetto a CPU")
        #plt.axhline(y=1, color='r', linestyle='--') # -> in questo caso le prestazioni sarebbero uguali
        #for x, y in zip(x_cpu, speedup):
        #    plt.annotate(f"{y:.1f}", (x, y), textcoords="offset points", xytext=(0,5), ha='center')
    plt.grid(True)
    plt.savefig(f"grafico_{label}.png")

def plot_confronto(x1, y1, label1, x2, y2, label2):
    plt.figure(figsize=(12, 6))  
    plt.plot(x1, y1, 'b', marker='o', label=label1)
    plt.plot(x2, y2, 'r', marker='o', label=label2)

    plt.xlabel('Distanza')
    plt.ylabel('Tempo medio di esecuzione (s)')
    #plt.xscale('log')
    #plt.yscale('log')
    plt.title('Confronto tempi medi GPU/CPU')
    plt.grid(True)
    plt.legend(loc='upper right')
    plt.savefig('Confronto_tempi_GPU_CPU')

### grafici tempi medi e metriche medie
#file_csv = "metriche_medie.csv"
file_csv = "tempi_medi_gpu.csv"
df = pd.read_csv(file_csv)

x = df["Distanza"]

for col in df.columns[1:]:
    plot(x, df[col], col)

### grafico confronto tempi medi GPU e CPU
gpu_file_csv = "tempi_medi_gpu.csv"
cpu_file_csv = "metriche_medie.csv"

df_gpu = pd.read_csv(gpu_file_csv)
df_cpu = pd.read_csv(cpu_file_csv)

x_gpu = df_gpu["Distanza"]
y_gpu = df_gpu["Tempo medio GPU (s)"]

x_cpu = df_cpu["Distanza"]
y_cpu = df_cpu["Tempo di esecuzione (s)"]

plot_confronto(x_gpu, y_gpu, "Tempi medi GPU (s)", x_cpu, y_cpu, "Tempi medi CPU (s)")

### grafico speedup
speedup = []
for i, d in enumerate(x_cpu):
    speedup.append(y_cpu[i]/y_gpu[i])
plot(x_cpu, speedup, "Speedup CPU - GPU")

