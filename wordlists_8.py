from pathlib import Path
from typing import List

def find_words_with_substring(sub: str,
                              #filename: str = "top_freq_5000_hu.txt"
                              # Az elérési út módosítandó !
                              filename=r"C:\Users\konyal\OneDrive - Budapesti Gazdasági Egyetem\Asztal\lili\ELTE\4. félév\git, sql\2. házi\words_practice_2425\word_lists\top_freq_5000_hu.txt") -> List[str]:

    """
    Listázza az összes olyan szót a megadott szólista‑fájlban,
    amely tartalmazza a 'sub' részszót (kis‑ és nagybetűre érzéketlenül).

    Paraméterek
    -----------
    sub : str
        A keresett részszó.
    filename : str, optional
        A szólista fájl elérési útja. Alapértelmezés: "top_freq_5000_hu.txt".
    ------------------
    List[str]
        A találati szavak listája (eredeti írásmóddal).
    """

    if not sub:
        raise ValueError("A keresett részszó nem lehet üres!")

    sub_lower = sub.lower()
    path = Path(filename)

    if not path.is_file():
        raise FileNotFoundError(f"A fájl nem található: {path}")

    matches: List[str] = []
    with path.open(encoding="utf-8") as f:
        for line in f:
            word = line.strip()
            if sub_lower in word.lower():
                matches.append(word)

    return matches


# Példa
if __name__ == "__main__":
    words = find_words_with_substring("kar")
    print(words)