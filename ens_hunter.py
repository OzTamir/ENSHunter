import sys
from web3 import Web3, HTTPProvider
from wordlist_generator import download_wordlist, get_common_words 
from config import CONFIG 

def get_wordlist(file_path):
    with open(file_path, 'r') as file:
        words = [word.strip() for word in file.readlines()]
    return words

def is_ens_available(word, w3):
    domain = word + '.eth'
    owner_address = w3.ens.owner(domain)
    return owner_address == '0x0000000000000000000000000000000000000000'

def generate_words():    
    current_words = 0
    download_wordlist()
    common_words = get_common_words()
    words = []
    for cool_word in CONFIG['cool_words']:
        for common_word in common_words:
            if len(common_word) < CONFIG['min_common_length']:
                continue
            combined_word = cool_word + common_word
            if CONFIG['min_length'] <= len(combined_word) <= CONFIG['max_length']:
                words.append(combined_word)
                current_words += 1
                if current_words >= CONFIG['max_words']:
                    return words
    
    return words

def main():
    if len(sys.argv) < 2:
        print("Usage: python ens_checker.py <wordlist_file> or python ens_checker.py --generate")
        sys.exit(1)

    if sys.argv[1] == "--generate":
        words = generate_words()
    else:
        wordlist_file = sys.argv[1]
        words = get_wordlist(wordlist_file)


    # Connect to Ethereum network (using Infura in this case, replace with your own API key)
    w3 = Web3(HTTPProvider('https://rpc.ankr.com/eth'))

    available_domains = []
    for word in words:
        if is_ens_available(word, w3):
            print(f'Available: {word}.eth')
            available_domains.append(word + '.eth')
        else:
            print(f'Unavailable: {word}.eth')

    if available_domains:
        print('-' * 50)
        print("Available ENS domains:")
        for domain in available_domains:
            print(domain)
    else:
        print("No available ENS domains found in the given wordlist.")

if __name__ == '__main__':
    main()
