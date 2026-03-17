import subprocess
import csv
import pandas as pd, io, os

num_esec = 2
proc = "test_cuStab.py"
distanze = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 84]

csv_tempi = "tempi.csv"

def elabora_tempi(csv_tempi):

    df = pd.read_csv(csv_tempi)

    media = df.groupby("Distanza", as_index=False)["Tempo (s)"].mean()
    media.rename(columns={"Tempo (s)": "Tempo medio (s)"}, inplace=True)

    media.to_csv("tempi_medi.csv", index=False)

with open(csv_tempi, "w") as f:
    # scrivo l'header del CSV Distanza, Tempo (s)
    f.write("Distanza,Tempo (s)\n")
    for d in distanze:
        for i in range(num_esec):
            
            print(f"Esecuzione {i+1}/{num_esec} per d={d}")

            result = subprocess.run(["python", proc, str(d)], capture_output=True, text=True)

            f.write(f"{d},{result.stdout.strip()}\n")

elabora_tempi(csv_tempi)