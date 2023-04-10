import sys
from web3 import Web3, HTTPProvider
from wordlist_generator import generate_words
from config import CONFIG

def get_wordlist(file_path):
    with open(file_path, 'r') as file:
        words = [word.strip() for word in file.readlines()]
    return words

def is_ens_available(word, w3):
    domain = word + '.eth'
    owner_address = w3.ens.owner(domain)
    return owner_address == '0x0000000000000000000000000000000000000000'

def run(words):
    w3 = Web3(HTTPProvider(CONFIG['rpc_url']))

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

def main():
    if len(sys.argv) < 2:
        print("Usage: python ens_hunter.py <wordlist_file> or python ens_hunter.py --generate [--nltk]")
        sys.exit(1)

    if sys.argv[1] == "--generate":
        if len(sys.argv) > 2:
            words = generate_words(sys.argv[2] == "--nltk")
        else:
            words = generate_words()
    else:
        wordlist_file = sys.argv[1]
        words = get_wordlist(wordlist_file)
        
    run(words)

if __name__ == '__main__':
    main()
