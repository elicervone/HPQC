''' per ncu
"ID" -> identifica il kernel
"Process ID" -> dc
"Process Name" -> dc
"Host Name" -> dc
"Kernel Name" -> nome del kernel CUDA eseguito  okay
"Context" -> bo forse?
"Stream" -> mi interessa sapere se è sempre lo stesso o no tra i vari kernel
"Block Size" -> mi interessa sapere se è sempre lo stesso o no per lo stesso kernel
"Grid Size" -> mi interessa sapere se è sempre lo stesso o no per lo stesso kernel
"Device" -> dc
"CC" -> dc
"Section Name" -> dc
"Metric Name" -> nome della metrica misurata  okay
"Metric Unit" -> unità di misura della metrica  okay
"Metric Value" -> valore della metrica misurata  okay 

Le colonne utili da tenere sono:
"ID", "Kernel Name", "Metric Name", "Metric Unit", "Metric Value" '''

import subprocess
import pandas as pd
import csv
import sys

csv_metriche = sys.argv[1]
d = int(sys.argv[2])

def elabora_metrche(csv_metriche):
    csv_medie = f'metriche_medie_{d}.csv'
    df = pd.read_csv(csv_metriche, usecols=["ID", "Kernel Name", "Metric Name", "Metric Unit", "Metric Value"])
    df["Metric Value"] = pd.to_numeric(df["Metric Value"], errors='coerce')

    # Media per (ID, Kernel Name, Metric Name, Metric Unit, distance)
    mean_df = (
        df.groupby(["ID", "Kernel Name", "Metric Name", "Metric Unit"], as_index=False).agg(Metric_Value_Mean=("Metric Value", "mean"))
    )

    # Crea colonna "Metric Name [Metric Unit]" e pivotta
    mean_df["Metric"] = mean_df["Metric Name"] + " [" + mean_df["Metric Unit"] + "]"
    pivot_df = mean_df.pivot_table(
        index=["ID", "Kernel Name"],
        columns="Metric",
        values="Metric_Value_Mean"
    ).reset_index()

    pivot_df.to_csv(csv_medie, index=False)
    #print(f"Medie salvate in {csv_medie}")

elabora_metrche(csv_metriche)