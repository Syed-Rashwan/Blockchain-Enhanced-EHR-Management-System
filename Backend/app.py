from flask import Flask, request, jsonify   
from web3 import Web3

app = Flask(__name__)

# Connect to local Ethereum node
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))

# Replace with your deployed contract address and ABI
contract_address = 'YOUR_CONTRACT_ADDRESS'
contract_abi = 'YOUR_CONTRACT_ABI'

contract = w3.eth.contract(address=contract_address, abi=contract_abi)

@app.route('/add_record', methods=['POST'])
def add_record():
    data = request.json
    patient_name = data['patientName']
    data_hash = data['dataHash']
    
    account = w3.eth.accounts[0]
    tx_hash = contract.functions.addRecord(patient_name, data_hash).transact({'from': account})
    w3.eth.waitForTransactionReceipt(tx_hash)
    
    return jsonify({'status': 'Record added'}), 200

@app.route('/get_records', methods=['GET'])
def get_records():
    account = w3.eth.accounts[0]
    records = contract.functions.getRecords().call({'from': account})
    return jsonify(records), 200

if __name__ == '__main__':
    app.run(debug=True)

