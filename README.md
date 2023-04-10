<div align="center">
  <a href="https://github.com/OzTamir/ENSHunter">
    <img src="https://app.ens.domains/static/media/ensIconLogo.19559e18fee46b91eb7a1b152d456d3b.svg"  width="300" height="150">
  </a>

  <h1 align="center">ENSHunter</h1>
</div>

This project provides a Python script to check the availability of ENS (Ethereum Name Service) domains based on a given wordlist or a generated wordlist with cool and common words.

## Requirements

- Python 3.9 (Due to compatibility issues with Web3.py, Python 3.10 is not recommended)
- Web3.py
- NLTK

To install the required libraries, run:

```bash
pip install web3 nltk
```

## Scripts
 - `ens_hunter.py`: This script checks the availability of ENS domains based on a given wordlist or a generated wordlist.
 - `wordlist_generator.py`: This script generates a wordlist containing combinations of cool and common words.

## Usage
### ens_hunter.py
To check the availability of ENS domains based on a given wordlist:
```bash
python ens_hunter.py wordlist.txt
```
To check the availability of ENS domains based on a generated wordlist:
```bash
python ens_hunter.py --generate
```

### wordlist_generator.py
To generate a wordlist containing combinations of cool and common words:

```bash
python wordlist_generator.py
```

## Note
Please be aware that checking a large number of ENS domains may take a significant amount of time and may hit rate limits if you're using a third-party Ethereum provider like Infura.

