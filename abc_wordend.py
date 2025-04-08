
words = []

with open("D:/Egyetem/01Ma_Survey/04felev/AdatInfr/words_practice_2425/word_lists/top_freq_5000_hu.txt", "r", encoding="utf-8") as f:
    for line in f:
        # Soron belül spliteljük a vesszőnél, majd eltávolítjuk a felesleges whitespace-eket
        words_in_line = [word.strip() for word in line.strip().split(",")]
        words.extend(words_in_line)

megfordit = []
for i in words:
    szo = i[::-1]
    megfordit.append(szo)

#print(megfordit)

megfordit.sort()
megfordit_abc = sorted(megfordit)

#print(megfordit_abc)

visszafordit = []
for i in megfordit_abc:
    szo = i[::-1]
    visszafordit.append(szo)

print(visszafordit)