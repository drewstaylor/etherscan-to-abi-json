#!/usr/bin/python3

'''
Export a contract's ABI JSON from an Etherscan verified contract
Supports mainnet and sepolia testnet
'''

from dotenv import dotenv_values
import argparse
import requests
import json

config = dotenv_values(".env")
api_key = config['ETHERSCAN_API_KEY']

parser = argparse.ArgumentParser()
parser.add_argument('addr', type=str, help='Contract address')
parser.add_argument('-o', '--output', type=str, help="Path to the output JSON file", required=True)
parser.add_argument('-t', '--testnet', type=bool, help="", required=False)

def __main__():
    args = parser.parse_args()

    if args.testnet is True:
        ABI_ENDPOINT = 'https://api-sepolia.etherscan.io/api?apikey='+ api_key +'&module=contract&action=getabi&address='
    else:
        ABI_ENDPOINT = 'https://api.etherscan.io/api?apikey='+ api_key +'&module=contract&action=getabi&address='

    response = requests.get('%s%s'%(ABI_ENDPOINT, args.addr))
    response_json = response.json()
    abi_json = json.loads(response_json['result'])
    result = json.dumps({
        "contract": args.addr,
        "abi": abi_json
    }, indent=4, sort_keys=True)

    open(args.output, 'w').write(result)

if __name__ == '__main__':
    __main__()