import sys
import requests
from web3 import Web3, HTTPProvider

def get_wordlist(file_path):
    with open(file_path, 'r') as file:
        words = [word.strip() for word in file.readlines()]
    return words

def is_ens_available(word, ens_contract):
    node = Web3.toChecksumAddress(ens_contract.functions.owner(Web3.sha3(text=word + '.eth')).call())
    return node == '0x0000000000000000000000000000000000000000'

def main():
    if len(sys.argv) < 2:
        print("Usage: python ens_checker.py <wordlist_file>")
        sys.exit(1)

    wordlist_file = sys.argv[1]
    words = get_wordlist(wordlist_file)

    # Connect to Ethereum network (using Infura in this case, replace with your own API key)
    w3 = Web3(HTTPProvider('https://rpc.ankr.com/eth'))

    # ENS Registry contract address
    ens_contract_address = '0x00000000000C2E074eC69A0dFb2997BA6C7d2e1e'

    # ENS Registry contract ABI (Application Binary Interface)
    # Only including the functions we need
    ens_abi = [
        {
            "constant": True,
            "inputs": [
                {
                    "name": "node",
                    "type": "bytes32"
                }
            ],
            "name": "owner",
            "outputs": [
                {
                    "name": "",
                    "type": "address"
                }
            ],
            "payable": False,
            "stateMutability": "view",
            "type": "function"
        }
    ]

    ens_contract = w3.eth.contract(address=ens_contract_address, abi=ens_abi)

    available_domains = []

    for word in words:
        if is_ens_available(word, ens_contract):
            available_domains.append(word + '.eth')

    if available_domains:
        print("Available ENS domains:")
        for domain in available_domains:
            print(domain)
    else:
        print("No available ENS domains found in the given wordlist.")

if __name__ == '__main__':
    main()
