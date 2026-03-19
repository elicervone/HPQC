import pandas as pd
import matplotlib.pyplot as plt

file_csv = "metriche_medie.csv"
df = pd.read_csv(file_csv)

x = df["Distanza"]

for col in df.columns[1:]:
    plt.figure()
    plt.plot(x, df[col], marker="o")
    plt.xlabel("Distanza")
    plt.ylabel(col)
    plt.title(f"{col} vs Distanza")
    plt.grid(True)
    plt.savefig(f"grafico_{col}.png")
    plt.close()
