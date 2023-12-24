# interface.py
import argparse
from blockchain import Blockchain, Block
from crypto import generate_key_pair, sign_transaction, verify_transaction
from transaction import Transaction

def create_genesis_block():
    blockchain = Blockchain()
    print("Genesis block created.")
    return blockchain

def view_blockchain(blockchain):
    print("\nBlockchain:")
    for block in blockchain.chain:
        print(f"Hash: {block.hash}")
        print(f"Previous Hash: {block.previous_hash}")
        print(f"Transactions: {block.transactions}")
        print("--------------")

def create_transaction(sender, recipient, amount, private_key, public_key, blockchain):
    transaction = Transaction(sender, recipient, amount)
    signature = sign_transaction(transaction, private_key)
    is_verified = verify_transaction(transaction, signature, public_key)
    if is_verified:
        block = Block("0")
        block.add_transaction(transaction)
        blockchain.add_block(block)
        print("Transaction added to the blockchain.")
    else:
        print("Transaction verification failed. Transaction not added.")

def main():
    parser = argparse.ArgumentParser(description="Simple Blockchain Interface")
    parser.add_argument("--generate-keypair", action="store_true", help="Generate RSA key pair")
    parser.add_argument("--create-genesis-block", action="store_true", help="Create the genesis block")
    parser.add_argument("--view-blockchain", action="store_true", help="View the current blockchain")
    parser.add_argument("--sender", help="Sender's name for creating a transaction")
    parser.add_argument("--recipient", help="Recipient's name for creating a transaction")
    parser.add_argument("--amount", type=float, help="Amount for creating a transaction")
    parser.add_argument("--private-key", help="Private key for signing a transaction")
    parser.add_argument("--public-key", help="Public key for verifying a transaction")  # Add this line
    
    args = parser.parse_args()

    if args.generate_keypair:
        private_key, public_key = generate_key_pair()
        print(f"Private Key: {private_key}")
        print(f"Public Key: {public_key}")
    
    if args.create_genesis_block:
        create_genesis_block()

    if args.view_blockchain:
        blockchain = Blockchain()
        view_blockchain(blockchain)

    if args.sender and args.recipient and args.amount and args.private_key and args.public_key:  # Update this line
        blockchain = Blockchain()
        create_transaction(args.sender, args.recipient, args.amount, args.private_key, args.public_key, blockchain)  # Update this line
        view_blockchain(blockchain)

if __name__ == "__main__":
    main()
