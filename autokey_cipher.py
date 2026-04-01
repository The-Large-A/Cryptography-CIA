ALPHABET_SIZE = 26

def char_to_num(c):
    return ord(c) - ord('A')

def num_to_char(n):
    return chr(n + ord('A'))

def preprocess(text):
    text = text.upper()
    return ''.join([c for c in text if c.isalpha()])

def generate_key(plaintext, key):
    key = preprocess(key)
    plaintext = preprocess(plaintext)
    key_extended = key + plaintext
    return key_extended[:len(plaintext)]

def encrypt(plaintext, key):
    plaintext = preprocess(plaintext)
    key_ext = generate_key(plaintext, key)
    ciphertext = ""
    for p, k in zip(plaintext, key_ext):
        c = (char_to_num(p) + char_to_num(k)) % ALPHABET_SIZE
        ciphertext += num_to_char(c)
    return ciphertext

def decrypt(ciphertext, key):
    ciphertext = preprocess(ciphertext)
    key = preprocess(key)
    plaintext = ""
    for i in range(len(ciphertext)):
        if i < len(key):
            k = key[i]
        else:
            k = plaintext[i - len(key)]
        p = (char_to_num(ciphertext[i]) - char_to_num(k)) % ALPHABET_SIZE
        plaintext += num_to_char(p)
    return plaintext