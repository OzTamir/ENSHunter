import nltk
from nltk.corpus import words
from config import CONFIG

def download_wordlist():
    nltk.download('words')

def get_common_words():
    common_words = set(words.words())
    return common_words

def generate_wordlist(cool_words, common_words, min_length, max_length, output_file, max_words):
    current_words = 0
    with open(output_file, 'w') as file:
        for cool_word in cool_words:
            for common_word in common_words:
                combined_word = cool_word + common_word
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
