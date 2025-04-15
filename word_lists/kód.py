from collections import Counter

with open ('proper_nouns_hu.txt', 'r', encoding = 'utf-8') as file1:
    proper_nouns = [line.strip() for line in file1 if line.strip()]
    
with open ('top_freq_5000_hu.txt', 'r', encoding = 'utf-8') as file2:
    top_freq = [line.strip() for line in file2 if line.strip()]

#párok gyűjtése

parok = []

for nev in proper_nouns:
    nev_lower = nev.lower()
    nev_counter = Counter(nev_lower)

    for szo in top_freq:
        if not nev_counter - Counter(szo):
            parok.append((nev, szo))
            break

for nev, szo in parok:
    print(f"{nev} <- {szo}\n")

#szótárba helyezés
parok_szotar = {nev: szo for nev, szo in parok}