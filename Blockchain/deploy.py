from web3 import Web3
from solcx import compile_source

# Connect to local Ethereum node
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))

# Compile the smart contract
contract_source_code = '''
<INSERT_SMART_CONTRACT_CODE_HERE>
'''
compiled_sol = compile_source(contract_source_code)
contract_id, contract_interface = compiled_sol.popitem()

# Deploy the contract
EHRManagement = w3.eth.contract(
    abi=contract_interface['abi'],
    bytecode=contract_interface['bin']
)

# Get the account to deploy the contract
account = w3.eth.accounts[0]

# Build and send the transaction
tx_hash = EHRManagement.constructor().transact({'from': account})
tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)

print(f"Contract deployed at address: {tx_receipt.contractAddress}")