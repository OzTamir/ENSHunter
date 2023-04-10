import nltk
from nltk.corpus import words

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
    cool_words = ['crypto', 'blockchain', 'decentralized', 'nft', 'defi', 'hodl', 'dao', 'daoism', 'daoist', 'ape']
    output_file = 'wordlist.txt'
    min_length = 4
    max_length = 8
    max_words = 100
    
    download_wordlist()
    common_words = get_common_words()

    generate_wordlist(cool_words, common_words, min_length, max_length, output_file, max_words)
    print(f"Generated wordlist saved to {output_file}")

if __name__ == '__main__':
    main()
