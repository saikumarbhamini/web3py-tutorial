from web3 import Web3

from env import INFURA_URL

infura_url = INFURA_URL
web3 = Web3(Web3.HTTPProvider(infura_url))
print(f"Connected: {web3.is_connected()}")
json_block_data = Web3.to_json(web3.eth.get_block('latest'))
acc = Web3.eth.account.create()
