ALPHABET_SIZE = 26
HASH_LENGTH = 8
ROUNDS = 3

def preprocess_hash(text):
    text = text.upper()
    return [ord(c) - ord('A') for c in text if c.isalpha()]

def autokey_expand(P, K):
    K_ext = K + P
    return K_ext[:len(P)]

def initial_transform(P, K_ext):
    return [(p + k) % ALPHABET_SIZE for p, k in zip(P, K_ext)]

def iterative_mix(C):
    L = len(C)
    for r in range(1, ROUNDS + 1):
        new_C = C.copy()
        for i in range(L):
            if i == 0:
                new_C[i] = (C[i] + r) % ALPHABET_SIZE
            else:
                new_C[i] = (C[i] + new_C[i - 1] + r) % ALPHABET_SIZE
        C = new_C
    return C

def compress(C):
    L = len(C)
    n = HASH_LENGTH
    b = (L + n - 1) // n
    H = [0] * n
    for j in range(b):
        for i in range(n):
            idx = j * n + i
            val = C[idx] if idx < L else 0
            H[i] = (H[i] + val) % ALPHABET_SIZE
    return H

def encode(H):
    return ''.join([chr(h + ord('A')) for h in H])

def custom_hash(text, key="KEY"):
    P = preprocess_hash(text)
    K = preprocess_hash(key)
    if len(P) == 0:
        return ""
    K_ext = autokey_expand(P, K)
    C = initial_transform(P, K_ext)
    C = iterative_mix(C)
    H = compress(C)
    return encode(H)