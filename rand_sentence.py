import random

proper_nouns = open("word_lists/proper_nouns_hu.txt" , encoding='utf-8').read().splitlines()
top_freq = open("word_lists/top_freq_5000_hu.txt", encoding='utf-8').read().splitlines()

def generate_random_sentence(total_words, num_proper_nouns):
    if num_proper_nouns > total_words:
        raise ValueError("A tulajdonnevek száma nem lehet nagyobb, mint az összes szó száma.")

    proper_words = random.choices(proper_nouns, k=num_proper_nouns)
    top_words = random.choices(top_freq, k=total_words - num_proper_nouns)

    all_words = proper_words + top_words
    random.shuffle(all_words)

    all_words[0] = all_words[0][0].upper() + all_words[0][1:]

    sentence = ' '.join(all_words)
    return sentence + '.'

print(generate_random_sentence(8, 2))