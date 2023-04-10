import sys
from web3 import Web3, HTTPProvider
from wordlist_generator import download_wordlist, get_common_words 
from config import CONFIG
from random import choice, shuffle
import itertools


def get_wordlist(file_path):
    with open(file_path, 'r') as file:
        words = [word.strip() for word in file.readlines()]
    return words

def is_ens_available(word, w3):
    domain = word + '.eth'
    owner_address = w3.ens.owner(domain)
    return owner_address == '0x0000000000000000000000000000000000000000'

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
    if len(sys.argv) < 2:
        print("Usage: python ens_checker.py <wordlist_file> or python ens_checker.py --generate")
        sys.exit(1)

    if sys.argv[1] == "--generate":
        if len(sys.argv) > 2:
            words = generate_words(sys.argv[2] == "--nltk")
        else:
            words = generate_words()
    else:
        wordlist_file = sys.argv[1]
        words = get_wordlist(wordlist_file)


    # Connect to Ethereum network (using Infura in this case, replace with your own API key)
    w3 = Web3(HTTPProvider('https://rpc.ankr.com/eth'))

    available_domains = []
    unavailable_domains = []
    for word in words:
        if is_ens_available(word, w3):
            print(f'Available: {word}.eth')
            available_domains.append(word + '.eth')
        else:
            print(f'Unavailable: {word}.eth')
            unavailable_domains.append(word + '.eth')

    if available_domains:
        print('-' * 50)
        print("Available ENS domains:")
        for domain in available_domains:
            print(domain)
    if unavailable_domains:
        print('-' * 50)
        print("Unavailable ENS domains:")
        for domain in unavailable_domains:
            print(domain)
    else:
        print("No available ENS domains found in the given wordlist.")

if __name__ == '__main__':
    main()
