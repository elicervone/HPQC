import subprocess
import csv
import pandas as pd, io, os

num_esec = 10
proc = "test_cuStab2.py"
#distanze = [5, 15, 25, 35, 45, 55, 65, 75, 84]
distanze = [55, 65, 75, 84]

NCU_METRICS = ",".join([
    "gpu__time_duration.sum",
    "gpu__compute_memory_throughput.avg.pct_of_peak_sustained_elapsed",
    "dram__cycles_active.avg",
    "dram__cycles_elapsed.avg",
    "gpu__dram_throughput.avg.pct_of_peak_sustained_elapsed",
    "sm__warps_active.avg.pct_of_peak_sustained_active",
])

def ncu(csv_metriche, header):
    result = subprocess.run([
            "ncu", "--metrics", NCU_METRICS, "--replay-mode", "application", "--target-processes", "all", "--csv", "python", proc, str(d)],
            capture_output=True, text=True,
    )
    # Salva il CSV da stdout
    with open(csv_metriche, "a") as f:
        if not header:
            f.write("\n".join(result.stdout.splitlines()[2:]) + "\n")
            header = True
        else:
            f.write("\n".join(result.stdout.splitlines()[3:]) + "\n")

    return header

def read_nsys_stats(rep_file, report_type):
    result = subprocess.run(
        ["nsys", "stats", "--force-export=true", "--report", report_type, "--format", "csv", rep_file],
        capture_output=True, text=True
    )
    
    if result.stderr.strip():
        print(f"  [STDERR] {result.stderr.strip()[:200]}")
    
    if not result.stdout.strip():
        return pd.DataFrame()
    
    # Salta righe di log (es. "Generating SQLite...") e trova l'header CSV
    lines = [l for l in result.stdout.splitlines() if "," in l]
    if not lines:
        return pd.DataFrame()
    
    return pd.read_csv(io.StringIO("\n".join(lines)))

def nsys():
    tag = f"d{d}_run{i+1}"
    rep_file = f"report_{tag}.nsys-rep"

    subprocess.run([
        "nsys", "profile",
        "--output", f"report_{tag}",
        "--force-overwrite=true",
        "--trace=cuda",
        "python", proc, str(d)
    ], check=True)

    kernels = read_nsys_stats(f"report_{tag}.nsys-rep", "cuda_gpu_kern_sum")
    mem_time = read_nsys_stats(f"report_{tag}.nsys-rep", "cuda_gpu_mem_time_sum")
    mem_size = read_nsys_stats(f"report_{tag}.nsys-rep", "cuda_gpu_mem_size_sum")

    # Salva i risultati in un CSV per kernels, mem_size e mem_time aggiungendo distanza e run come colonne
    for df, name in [(kernels, "nsys_kernels"), (mem_time, "nsys_mem_time"), (mem_size, "nsys_mem_size")]:
        if df.empty:
            continue
        df["d"] = d
        df["run"] = i + 1
    
        # Scrivi header solo se il file non esiste ancora
        file_esiste = os.path.exists(f"{name}.csv")
        df.to_csv(f"{name}.csv", mode="a", header=not file_esiste, index=False)
        #print(f"  → {name}.csv aggiornato ({len(df)} righe aggiunte)")

for d in distanze:
    
    #  file ncu
    csv_metriche = f"ncu_metriche_{d}.csv"
    header = False
    for i in range(num_esec):
        
        print(f"Esecuzione {i+1}/{num_esec} per d={d}")

        # nsight compute
        header = ncu(csv_metriche, header)

        # nsight systems
        nsys()

    # Elabora CSV ncu
    print(f"\nElaborazione CSV NCU per d={d}:")
    result = subprocess.run(["python", "elab_ncu.py", csv_metriche, str(d)], capture_output=True, text=True)
    print(result.stdout)

    # Elabora CSV nsys
    print(f"\nElaborazione CSV NSYS per d={d}:")
    result = subprocess.run(["python", "elab_nsys.py"], capture_output=True, text=True)
    print(result.stdout)