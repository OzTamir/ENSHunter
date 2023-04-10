import nltk
from nltk.corpus import words
from config import CONFIG
from random import choice, shuffle
import itertools

def download_wordlist():
    nltk.download('words')
    nltk.download('averaged_perceptron_tagger') 

def get_common_words():
    all_words = set(words.words())
    tagged_words = nltk.pos_tag(list(all_words))
    adjectives = set(word for word, pos in tagged_words if pos == 'JJ')
    return adjectives

def write_wordlist_to_file(wordlist, output_file):
    with open(output_file, 'w') as file:
        for word in wordlist:
            file.write(word + '\n')

def get_words_for_cool_word(cool_word, common_words, max_words):
    words = []
    current_words = 0
    for common_word in common_words:
        if len(common_word) < CONFIG['min_common_length']:
            continue
        combined_word = choice([cool_word + common_word, common_word + cool_word])
        if CONFIG['min_length'] <= len(combined_word) <= CONFIG['max_length']:
            words.append(combined_word)
            current_words += 1
            if current_words >= max_words:
                return words
    return words

def generate_words(use_nltk=True):    
    words = []
    if use_nltk:
        download_wordlist()
        common_words = get_common_words()
        for cool_word in CONFIG['cool_words']:
            words += get_words_for_cool_word(cool_word, common_words, CONFIG['max_words'])
    words += [''.join(x) for x in list(itertools.combinations(CONFIG['cool_words'], 2))]
    shuffle(words)
    return words

def main():
    words = generate_words()
    write_wordlist_to_file(words, CONFIG['output_file'])
    print(f"Generated wordlist saved to {CONFIG['output_file']}")

if __name__ == '__main__':
    main()
