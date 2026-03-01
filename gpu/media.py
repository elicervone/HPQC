''' calcolo del tempo medio di esecuzione del circuito '''

import sys

d = int(sys.argv[1])

with open(f"time_{d}.txt", "r") as f:
    tempi = [float(line.strip().split()[1]) for line in f]

    # calcolo media con 10 cifre decimali
    media = sum(tempi) / len(tempi)
    print(f"Tempo medio di simulazione per d={d}: {media:.10f} secondi")

    deviazione_standard = (sum((x - media) ** 2 for x in tempi) / len(tempi)) ** 0.5
    print(f"Deviazione standard: {deviazione_standard:.10f} secondi")