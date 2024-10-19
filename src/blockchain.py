from web3 import Web3
import json

w3 = Web3(Web3.HTTPProvider('https://base.rpc.url'))

contract_address = '0xYourContractAddress'
with open('contracts/ContentOwnership.json') as f:
    contract_abi = json.load(f)

contract = w3.eth.contract(address=contract_address, abi=contract_abi)

def register_content(content_hash):
    account = w3.eth.account.privateKeyToAccount('your_private_key')
    tx = contract.functions.registerContent(content_hash).buildTransaction({
        'from': account.address,
        'nonce': w3.eth.getTransactionCount(account.address),
        'gas': 2000000,
        'gasPrice': w3.toWei('50', 'gwei')
    })
    signed_tx = w3.eth.account.signTransaction(tx, 'your_private_key')
    tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    return w3.toHex(tx_hash)

def get_content_owner(content_hash):
    return contract.functions.getContentOwner(content_hash).call()
