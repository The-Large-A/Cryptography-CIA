# Autokey Cipher and Custom Hash Function Implementation

## Aim

To implement the Auto Key Cipher (encryption and decryption) along with a custom-designed hashing function based on Autokey principles, without using any built-in cryptographic libraries.

---

## Theory

### Autokey Cipher

The Autokey Cipher is a classical substitution cipher where the key is extended using the plaintext itself. This removes periodic repetition and improves security compared to simple repeating-key ciphers.

Encryption formula:
C[i] = (P[i] + K[i]) mod 26

Decryption formula:
P[i] = (C[i] - K[i]) mod 26

---

### Custom Hash Function

The hashing function is designed using concepts from the Autokey Cipher and includes the following stages:

1. Preprocessing – Convert input into numeric format (A=0 to Z=25)
2. Autokey Expansion – Extend key using plaintext
3. Transformation – Apply modular addition
4. Iterative Mixing – Multiple rounds to increase diffusion
5. Compression – Reduce variable length to fixed size
6. Encoding – Convert numeric hash to string

---

## Justification of Hash Design

The custom hash function was chosen because:

* It demonstrates understanding of cryptographic concepts
* Uses diffusion and confusion principles
* Produces fixed-length output
* Does not rely on external libraries
* Ensures deterministic and irreversible mapping through compression

---

## Algorithm Overview

1. Normalize input (uppercase, remove non-alphabet characters)
2. Convert characters to numeric values
3. Extend key using Autokey method
4. Perform modular transformation
5. Apply iterative mixing for multiple rounds
6. Compress into fixed-length hash using block summation
7. Convert result back to characters

---

## How to Run

1. Make sure Python is installed

2. Place all files in the same folder

3. Run the program:

   python test_script.py

4. Enter the required inputs when prompted:

   * Plaintext
   * Key

---

## Example Run

Enter plaintext: HELLO WORLD
Enter key: KEY

Ciphertext: RIJVSUYVJN
Hash: XXXXXXXX
Decrypted Text: HELLOWORLD

---

## Files Included

* autokey_cipher.py → encryption and decryption
* custom_hash.py → hashing function
* test_script.py → user-input based execution
* README.md → documentation

---

## Constraints Followed

* No cryptographic libraries used
* Entire implementation done from scratch
* Hash function is custom-designed and not from standard libraries

---

## Limitations / Implementation Challenges

* The hash function is not cryptographically secure and is intended only for academic purposes
* Since compression reduces data size, collisions (different inputs producing the same hash) may occur
* The algorithm only supports alphabetic input (A–Z), requiring preprocessing of input data
* Choosing appropriate values for hash length and number of mixing rounds affects performance and output quality
* Iterative mixing introduces dependency between elements, which can increase computational complexity for large inputs

---
