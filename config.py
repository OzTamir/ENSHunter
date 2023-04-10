from random import shuffle

cool_words = [
    'crypto',
    'blockchain',
    'decentralized',
    'nft',
    'defi',
    'hodl',
    'dao',
    'daoism',
    'daoist',
    'ape',
    'ether',
    'ethereum',
    'eth',
    'super',
    'hyper',
    'king',
    'queen',
    'prince',
    'lord',
    'punk',
    'bit',
    'chain'
]
shuffle(cool_words)

CONFIG = {
    'cool_words': cool_words,
    'min_length': 4,
    'max_length': 8,
    'min_common_length': 4,
    'max_words': 25,
    'output_file': 'wordlist.txt',
    'rpc_url': 'https://rpc.ankr.com/eth'
}