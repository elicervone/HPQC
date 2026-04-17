d = 35

with open(f"tempi_{d}.txt", "r", encoding="utf-16") as f:
    lines = f.readlines()
    tempi = [float(line.strip().split()[2]) for line in lines]

    media = sum(tempi) / len(tempi)
    print(f"Media dei tempi per d={d}: {media} secondi")

    stdev = (sum((x - media) ** 2 for x in tempi) / len(tempi)) ** 0.5
    print(f"Deviazione standard dei tempi per d={d}: {stdev} secondi")