def remove_stopwords(freq_file_path, stopwords_file_path):

    stopwords = set()

    with open(stopwords_file_path, 'r', encoding='utf-8') as stop_file:
        for line in stop_file:
            parts = line.strip().replace(',', '').split()
            stopwords.update(parts)

    words = []

    with open(freq_file_path, 'r', encoding='utf-8') as freq_file:
        for line in freq_file:
            parts = line.strip().replace(',', '').split()
            words.extend(parts)

    filtered_words = []

    for word in words:
        if word and word not in stopwords:
            filtered_words.append(word)

    return filtered_words

filtered = remove_stopwords('word_lists/top_freq_5000_hu.txt', 'word_lists/stopwords_hu.txt')
print(f"a leggyakoribb szavak száma a stopszavaj nélkül : {len(filtered)}")
print(f"első 10 szó : {filtered[:10]}")

