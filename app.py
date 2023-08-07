from web3 import Web3


http_provider_url = 'https://mainnet.infura.io/v3/568055971b6e4859bb3265e35d24fba8'
web3 = Web3(Web3.HTTPProvider(http_provider_url))
print(f"Connected: {web3.is_connected()}")
json_block_data = Web3.to_json(web3.eth.get_block('latest'))
acc = Web3.eth.account.create()
