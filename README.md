# Etherscan to ABI JSON

Fetches ABI json for any verified contract uploaded to mainnet or sepolia Etherscan

## Usage

```sh
./fetch_abi.py <contract address> --output <string: output path> --testnet <boolean: use testnet>
# E.g.:
# ./fetch_abi.py 0x16efda168bde70e05ca6d349a690749d622f95e0 -o ./output/wbtc.abi.json -t true 
```
