### Seconda versione in cui salvo tutte le metriche e poi le elaboro ###
import subprocess
import json
import csv
import pandas as pd

from numpy import mean

num_esec = 5
proc = "provastim.py"
distanze = [5, 10, 15, 20, 25]
distanze = [30, 35, 40]
distanze = [45, 50]
#distanze = [5, 10, 15]

def formatta_metriche(output, tempo, d):
    metriche_dict = {}

    metriche_dict["Distanza"] = d
    metriche_dict["Tempo di esecuzione (s)"] = tempo
    
    # ignora la prima metrica command being timed e passa direttamente alla seconda
    # ignora anche l'ultima metrica
    for line in output.splitlines()[1:-1]:
        #print("Linea metrica: ", line)
        if "Elapsed (wall clock) time" in line:
            met = "Elapsed (wall clock) time (s)"
            parts = line.split(":")[4:]

            if len(parts) == 3:
                ore, min, sec = line.split(":")[4:]
                val = str(int(ore.strip()) * 3600 + int(min.strip()) * 60 + float(sec.strip()))
            elif len(parts) == 2:
                min, sec = line.split(":")[4:]
                val = str(int(min.strip()) * 60 + float(sec.strip()))
            else:
                val = line.split(":")[4].strip()
        else:
            met, val = line.split(":", 1)
            met = met.strip()
            val = val.strip()
            if "%" in val:
                val = val.replace("%", "").strip()
                met = met + " (%)"

        metriche_dict[met] = val
    
    return metriche_dict

def raccolta_metriche():        
    
    # creo il file csv per le metriche
    metriche_csv = "metriche.csv"
    header_scritto = False

    with open(metriche_csv, "w", newline='') as csvfile:

        # variabile per tenere traccia del writer e scrivere l'header solo alla prima esecuzione
        writer = None

        for d in distanze:    
        
            print("\n \n", f"Valore di distanza: {d}")

            for i in range(num_esec):
                print(f"Esecuzione {i+1}/{num_esec}...")
                
                result = subprocess.run(
                    ["/usr/bin/time", "-v", "python", proc, str(d)],
                    capture_output=True, text=True,
                )

                tempo = float(result.stdout.strip())

                print("Tempo di esecuzione: ", tempo, "secondi")
                #print("Metriche raccolte: ", metriche)
                #print("Output: ", result.stderr)

                metriche_dict = formatta_metriche(result.stderr, tempo, d)

                # crea il writer dopo aver visto le colonne
                if not header_scritto:
                    writer = csv.DictWriter(csvfile, fieldnames=metriche_dict.keys())
                    writer.writeheader()
                    header_scritto = True

                writer.writerow(metriche_dict)

                #print("Metriche raccolte: ", metriche_dict)

def media_metriche(colonne):
    # leggi il csv
    df = pd.read_csv("metriche1.csv")

    # calcola la media per ogni distanza
    medie = df.groupby("Distanza")[colonne].mean(numeric_only=True)

    medie.to_csv("metriche_medie.csv")   # salva il csv con le medie

def devstd_metriche(colonne):
    # leggi il csv
    df = pd.read_csv("metriche.csv")

    # calcola la deviazione standard per ogni distanza
    devstd = df.groupby("Distanza").std(numeric_only=True)

    devstd.to_csv("metriche_devstd.csv")   # salva il csv con le deviazioni standard

if __name__ == "__main__":
    #raccolta_metriche()
    colonne = ["Tempo di esecuzione (s)", "User time (seconds)", "System time (seconds)", "Percent of CPU this job got (%)", "Elapsed (wall clock) time (s)", 
               "Maximum resident set size (kbytes)", "Minor (reclaiming a frame) page faults"]
    media_metriche(colonne)
    #devstd_metriche(colonne)


''' METRICHE CHE VALGONO SEMPRE 0
- Average shared text size (kbytes)
- Average unshared data size (kbytes)
- Average stack size (kbytes)
- Average total size (kbytes)
- Average resident set size (kbytes)
- Swaps
- File system outputs
- Socket messages sent
- Socket messages received
- Signals delivered
- Page size (bytes) => VALE SEMPRE 4096'''