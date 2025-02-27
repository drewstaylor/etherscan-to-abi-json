# Etherscan to ABI JSON

Fetches ABI json for any verified contract uploaded to mainnet or sepolia Etherscan

## Setup

```sh
cp env.example .env
# Now add your Etherscan API key to .env
# More info @: https://docs.etherscan.io/getting-started/viewing-api-usage-statistics#creating-an-api-key
```

## Usage

```sh
usage: fetch_abi.py [-h] -o OUTPUT [-t TESTNET] addr

positional arguments:
  addr                  Contract address

options:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Path to the output JSON file
  -t TESTNET, --testnet TESTNET
```

## Example

```sh
./fetch_abi.py <contract address> --output <string: output path> --testnet <boolean: use testnet>
# E.g.:
# ./fetch_abi.py 0x16efda168bde70e05ca6d349a690749d622f95e0 -o ./output/wbtc.abi.json -t true 
```
