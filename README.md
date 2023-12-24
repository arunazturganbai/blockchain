# Blockchain Application

This is a simple implementation of a blockchain application with the following features:

## Asymmetric Encryption Implementation

The code includes a manual implementation of asymmetric encryption without using pre-existing libraries. The encryption is utilized for securing transactions in the blockchain.

## Digital Signature Implementation

A digital signature mechanism is developed using the encryption method from Task 1. This ensures the authenticity and integrity of transactions in the blockchain.

## Blockchain Application Development

### User Interface

A Command Line Interface (CLI) is provided for users to interact with the blockchain. The CLI supports various commands for generating key pairs, creating the genesis block, viewing the blockchain, and creating transactions.

### Examples

#### Generate RSA Key Pair

```bash
python interface.py --generate-keypair

Output:
Private Key: -----BEGIN RSA PRIVATE KEY-----
...
-----END RSA PRIVATE KEY-----

Public Key: -----BEGIN RSA PUBLIC KEY-----
...
-----END RSA PUBLIC KEY-----

This command generates an RSA key pair and prints the private and public keys.

Create Genesis Block
python interface.py --create-genesis-block
Output:
Genesis block created.

This command creates the genesis block of the blockchain.

View Blockchain
python interface.py --view-blockchain
Output:
Blockchain:
Hash: ...
Previous Hash: 0
Transactions: []
--------------

This command displays the current state of the blockchain.

Create Transaction
python interface.py --sender Alice --recipient Bob --amount 10 --private-key <your_private_key> --public-key <your_public_key>
Output:
Transaction added to the blockchain.

This command creates and adds a new transaction to the blockchain.

Dependencies
Python 3.x
Crypto library (install using pip install pycryptodome)
