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

import re
import subprocess
import pandas as pd
import csv
import sys
import glob
import os

distanze = [5, 10, 15, 25, 35, 45]

def unisci_metriche():
    output = 'metriche_ncu.csv'

    with open(output, 'a', newline='') as out_file:
        writer = csv.writer(out_file)
        colonne = ["Distanza", "ID", "Kernel Name", "Metric Name", "Metric Unit", "Metric Value"]
        writer.writerow(colonne)

        for d in distanze:
            file = f'ncu_metriche_{d}.csv'
            if os.path.exists(file):
                with open(file, 'r') as in_file:
                    reader = csv.reader(in_file)
                    header = next(reader)

                    idx = {col: i for i, col in enumerate(header)}

                    for row in reader:
                        filtered = [row[idx[c]] for c in colonne[1:]]
                        writer.writerow([d] + filtered)

            else:
                print(f"File {file} non trovato.")  

def media_metriche():
    df = pd.read_csv('metriche_ncu.csv')

    df["Metric Value"] = pd.to_numeric(df["Metric Value"], errors="coerce")

    metriche_medie = (
        df.groupby(
            ["Distanza", "ID", "Kernel Name", "Metric Name", "Metric Unit"],
            as_index=False
        )["Metric Value"]
        .mean()
    )

    metriche_medie.rename(columns={"Metric Value": "Metric Value Media"}, inplace=True)

    metriche_medie.to_csv('metriche_medie_ncu.csv', index=False)

    devstd_metriche = (
        df.groupby(
            ["Distanza", "ID", "Kernel Name", "Metric Name", "Metric Unit"],
            as_index=False
        )["Metric Value"]
        .std()
    )

    devstd_metriche.rename(columns={"Metric Value": "Metric Value DevStd"}, inplace=True)

    devstd_metriche.to_csv('metriche_devstd_ncu.csv', index=False)

def coeff_var():
    df_medie = pd.read_csv('metriche_medie_ncu.csv')
    df_devstd = pd.read_csv('metriche_devstd_ncu.csv')

    # uso lo stesso formato, ma senza la colonna metric value media
    df_coeff_var = df_medie.drop(columns=["Metric Unit", "Metric Value Media"])

    df_coeff_var["Coefficiente di Variazione"] = (df_devstd["Metric Value DevStd"] / df_medie["Metric Value Media"]) * 100

    df_coeff_var.to_csv('metriche_coeff_var_ncu.csv', index=False)


def separa_file():
    df = pd.read_csv('metriche_medie_ncu.csv')

    df["Metric"] = df["Metric Name"] + " [" + df["Metric Unit"] + "]"

    for (id_val, kernel_name), gruppo in df.groupby(["ID", "Kernel Name"]):

        pivot = gruppo.pivot_table(
            index="Distanza",
            columns="Metric",
            values="Metric Value Media"
        ).reset_index()

        kernel = kernel_name.split('(')[0]  # prendi solo il nome del kernel senza i parametri

        if '<' in kernel:
            kernel = kernel.split('<')[0]  # rimuovi eventuali template parameters
            
        filename = f"{kernel}_{id_val}.csv"
        pivot.to_csv(filename, index=False)

        print(f"Creato: {filename}")

#unisci_metriche()
#media_metriche()
#coeff_var()
separa_file()
