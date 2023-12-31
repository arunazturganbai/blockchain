from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

def generate_key_pair():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

def sign_transaction(transaction, private_key):
    key = RSA.import_key(private_key)
    h = SHA256.new(str(transaction.__dict__).encode())
    signature = pkcs1_15.new(key).sign(h)
    return signature

def verify_transaction(transaction, signature, public_key):
    key = RSA.import_key(public_key)
    h = SHA256.new(str(transaction.__dict__).encode())
    try:
        pkcs1_15.new(key).verify(h, signature)
        return True
    except (ValueError, TypeError):
        return False
