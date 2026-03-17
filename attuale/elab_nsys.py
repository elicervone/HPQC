import pandas as pd

def elabora(filepath, chiave_gruppo, colonne_medie):

    #print(f"\nElaborazione {filepath}...")

    df = pd.read_csv(filepath)

    #print(f"→ Caricato {filepath} con {len(df)} righe")

    #print(f"\n[{filepath}] Colonne disponibili: {df.columns.tolist()}")
    
    # Calcola media per (chiave_gruppo + distanza)
    gruppi = chiave_gruppo + ["d"]
    mean_df = df.groupby(gruppi)[colonne_medie].mean().reset_index()
    
    out = filepath.replace(".csv", f"_media.csv")
    mean_df.to_csv(out, index=False)
    #print(f"→ Salvato {out}")
    #print(mean_df.to_string(index=False))
    return mean_df


# --- Kernels ---
kernels_mean = elabora(
    filepath="nsys_kernels.csv",
    chiave_gruppo=["Name"],
    colonne_medie=["Time (%)", "Total Time (ns)", "Avg (ns)", "Min (ns)", "Max (ns)"],
)

# --- Memory time ---
mem_time_mean = elabora(
    filepath="nsys_mem_time.csv",
    chiave_gruppo=["Operation"],
    colonne_medie=["Time (%)", "Total Time (ns)", "Avg (ns)", "Min (ns)", "Max (ns)"],
)

# --- Memory size ---
mem_size_mean = elabora(
    filepath="nsys_mem_size.csv",
    chiave_gruppo=["Operation"],
    colonne_medie=["Total (MB)", "Avg (MB)", "Min (MB)", "Max (MB)"],
)

# --- Unisci mem_time e mem_size in un unico file ---
memory_mean = pd.merge(mem_time_mean, mem_size_mean, on=["Operation", "d"], how="outer")
memory_mean.to_csv("nsys_memory_mean.csv", index=False)
#print("\n→ Salvato nsys_memory_mean.csv")
#print(memory_mean.to_string(index=False))