# blockchain.py
import hashlib
import time
from crypto import generate_key_pair, sign_transaction, verify_transaction
from transaction import Transaction

class Block:
    def __init__(self, previous_hash):
        self.transactions = []
        self.previous_hash = previous_hash
        self.timestamp = time.time()
        self.nonce = 0
        self.hash = self.calculate_hash()

    def add_transaction(self, transaction):
        self.transactions.append(transaction)
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = (
            str(self.timestamp)
            + str(self.transactions)
            + str(self.previous_hash)
            + str(self.nonce)
        )
        return hashlib.sha256(block_string.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block("0")

    def get_last_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_last_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

# Example Usage
private_key, public_key = generate_key_pair()
blockchain = Blockchain()

# Create a transaction
transaction = Transaction("Alice", "Bob", 10)

# Sign the transaction
signature = sign_transaction(transaction, private_key)

# Verify the signature
is_verified = verify_transaction(transaction, signature, public_key)
print(f"Is Transaction Verified? {is_verified}")

# Create a block and add the transaction
block = Block("0")
block.add_transaction(transaction)
blockchain.add_block(block)

# Print the blockchain
for block in blockchain.chain:
    print(f"Hash: {block.hash}")
    print(f"Previous Hash: {block.previous_hash}")
    print(f"Transactions: {block.transactions}")
    print("--------------")
