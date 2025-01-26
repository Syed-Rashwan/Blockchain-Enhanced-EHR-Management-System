import json
from web3 import Web3

def load_network_config(network_name):
    with open(f'network/{network_name}.json') as f:
        return json.load(f)

def interact_with_contract(network_name, contract_address, abi):
    config = load_network_config(network_name)
    w3 = Web3(Web3.HTTPProvider(config['url']))
    
    contract = w3.eth.contract(address=contract_address, abi=abi)
    
    # Example interaction: Call a function from the contract
    result = contract.functions.yourFunctionName().call()
    print(f"Result from contract function: {result}")

if __name__ == "__main__":
    interact_with_contract('development', '0xYOUR_CONTRACT_ADDRESS', '[]')  # Replace with actual ABI