from autokey_cipher import encrypt, decrypt
from custom_hash import custom_hash

def run_test():
    plaintext = input("Enter plaintext: ")
    key = input("Enter Key: ")

    cyphertext = encrypt(plaintext, key)
    hash = custom_hash(cyphertext)
    decrypted = decrypt(cyphertext, key)

    print("Encoding plaintext using custom hash function:")
    print("Plaintext:", plaintext)
    print("Ciphertext:", cyphertext)
    print("Hash:", hash)
    print("Decrypted:", decrypted)

if __name__ == "__main__":
    run_test()