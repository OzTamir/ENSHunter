import nltk
from nltk.corpus import words
from config import CONFIG
from random import choice

def download_wordlist():
    nltk.download('words')
    nltk.download('averaged_perceptron_tagger') 

def get_common_words():
    all_words = set(words.words())
    tagged_words = nltk.pos_tag(list(all_words))
    adjectives = set(word for word, pos in tagged_words if pos == 'JJ')
    return adjectives

def generate_wordlist(cool_words, common_words, min_length, max_length, output_file, max_words):
    current_words = 0
    with open(output_file, 'w') as file:
        for cool_word in cool_words:
            for common_word in common_words:
                combined_word = choice([cool_word + common_word, common_word + cool_word])
                if min_length <= len(combined_word) <= max_length:
                    file.write(combined_word + '\n')
                    current_words += 1
                    if current_words >= max_words:
                        return

def main():
    download_wordlist()
    common_words = get_common_words()
    
    generate_wordlist(CONFIG['cool_words'], common_words, CONFIG['min_length'], CONFIG['max_length'], CONFIG['output_file'], CONFIG['max_words'])
    print(f"Generated wordlist saved to {CONFIG['output_file']}")

if __name__ == '__main__':
    main()
