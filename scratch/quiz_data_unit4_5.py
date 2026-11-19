# -*- coding: utf-8 -*-
"""
Quiz data, solution keys, and detailed mathematical explanations
for Mathematics Modules 18 to 29 (Unit IV & Unit V).
"""

from extract_questions_18_29 import parse_module_questions
import os

# Solution indices (0: A, 1: B, 2: C, 3: D)
MATHS_SOLUTIONS_18_29 = {
    18: [1, 2, 1, 2, 0, 2, 1, 1, 1, 1, 0, 1],
    19: [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1],
    20: [2, 1, 1, 2, 3, 2, 2, 1, 0, 1, 1, 1],
    21: [1, 1, 3, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1],
    22: [1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    23: [1, 1, 1, 1, 1, 1, 2, 1, 0, 2, 0, 2, 1, 1],
    24: [1, 1, 1, 2, 2, 0, 1, 1, 1, 1, 1, 1],
    25: [1, 1, 0, 2, 2, 1, 1, 2, 1, 0, 0, 2, 1, 1],
    26: [1, 1, 0, 2, 0, 2, 2, 1],
    27: [0, 1, 0, 1, 2, 1, 1, 0],
    28: [1, 0, 1, 2, 0, 1, 0, 1, 2, 1],
    29: [1, 2, 2, 1, 1, 1, 1, 1]
}

EXPLANATIONS_18_29 = {
    18: {
        1: "Cryptography is the science and study of transforming messages so they cannot easily be read or recovered without special authorization or keys.",
        2: "The original intelligible unencrypted message is defined mathematically as the Plaintext P.",
        3: "Decryption is the mathematical inverse function D_k(C) = P that recovers plaintext from ciphertext.",
        4: "The Caesar cipher is named after Julius Caesar, who used a fixed 3-position shift to protect military messages.",
        5: "In a substitution cipher, letters or symbols are systematically replaced by other letters or symbols.",
        6: "A transposition (permutation) cipher preserves letter identities but rearranges their positional order.",
        7: "Cryptanalysis is the study of breaking cryptosystems and recovering plaintexts without knowing the secret key.",
        8: "The shift cipher is a symmetric private-key cipher where sender and receiver share the same secret key.",
        9: "In asymmetric public-key cryptography, the recipient's private key is kept strictly confidential.",
        10: "The Diffie-Hellman protocol allows two distant parties to securely agree on a shared secret key over an insecure channel.",
        11: "In a Caesar cipher (+3 shift), letter X (index 23) becomes (23 + 3) mod 26 = 26 mod 26 = 0, which corresponds to A.",
        12: "The RSA cryptosystem was published in 1977 by Ron Rivest, Adi Shamir, and Leonard Adleman."
    },
    19: {
        1: "A monoalphabetic substitution cipher uses one fixed permutation mapping of the alphabet across the entire message.",
        2: "A reversible cipher function must be bijective (both injective / one-to-one and surjective / onto) so every ciphertext letter maps back to a unique plaintext letter.",
        3: "There are 26! (approximately 4.03 × 10²⁶) possible bijective permutations of a 26-letter alphabet.",
        4: "Monoalphabetic substitution preserves the exact statistical frequency distribution of the plaintext language.",
        5: "In standard English text, letter E is the most common with an average frequency of approximately 12.7%.",
        6: "A character cipher operates on individual characters one at a time, whereas a block cipher encrypts blocks of letters simultaneously.",
        7: "Substitution replaces letter identities; transposition reorders letter positions without altering their identities.",
        8: "Letter frequencies are invariant under simple substitution because each plaintext letter always produces the same ciphertext letter.",
        9: "Digrams are pairs of consecutive letters; common English digrams include TH, HE, IN, ER, AN.",
        10: "Trigrams are three consecutive letters; the most frequent English trigram is THE.",
        11: "A polyalphabetic cipher varies the substitution rule throughout the message, flattening frequency spikes.",
        12: "Frequency analysis breaks monoalphabetic ciphers by matching the most frequent ciphertext letters to English frequency tables."
    },
    20: {
        1: "In standard number-theoretic alphabet indexing starting from A = 0, Z has the value 25.",
        2: "Shift cipher encryption is defined by c ≡ (p + k) mod 26.",
        3: "Shift cipher decryption is defined by p ≡ (c - k) mod 26.",
        4: "X has numerical value 23. (23 + 5) mod 26 = 28 mod 26 = 2, which corresponds to C.",
        5: "C has numerical value 2. (2 - 5) mod 26 = -3 mod 26 = 23, which corresponds to X.",
        6: "D is 3 and J is 9. Key k = (9 - 3) mod 26 = 6.",
        7: "The Caesar cipher is specifically the shift cipher with key k = 3.",
        8: "There are 26 possible shift keys in ℤ₂₆: {0, 1, 2, ..., 25}.",
        9: "K(10)→H(7), H(7)→E(4), O(14)→L(11), O(14)→L(11), R(17)→O(14). The recovered plaintext is HELLO.",
        10: "A brute force attack on a shift cipher requires testing at most 25 non-trivial keys.",
        11: "The shift cipher is insecure because its keyspace is extremely small (only 26 keys) and it preserves letter frequencies.",
        12: "If k = 0, E₀(p) = p mod 26, leaving the plaintext completely unchanged."
    },
    21: {
        1: "The affine encryption formula is c ≡ (ap + b) mod 26.",
        2: "The multiplier a must be coprime to the alphabet size: gcd(a, 26) = 1, ensuring a modular multiplicative inverse exists.",
        3: "13 is not coprime to 26 since gcd(13, 26) = 13 ≠ 1.",
        4: "K is 10. f(10) = (7·10 + 3) mod 26 = 73 mod 26 = 21, which corresponds to V.",
        5: "7 × 15 = 105 = 4 × 26 + 1 ≡ 1 (mod 26), so the multiplicative inverse is 15.",
        6: "Affine decryption is given by p ≡ a⁻¹(c - b) mod 26.",
        7: "There are φ(26) = φ(2)·φ(13) = 1 · 12 = 12 integers in ℤ₂₆ coprime to 26.",
        8: "There are 12 choices for a and 26 choices for b, giving 12 × 26 = 312 total affine keys.",
        9: "When a = 1, the affine cipher c ≡ (1p + b) mod 26 reduces to the shift cipher with key b.",
        10: "The inverse of 3 modulo 26 is 9, because 3 × 9 = 27 ≡ 1 mod 26.",
        11: "Knowing two plaintext-ciphertext letter pairs allows solving a system of two linear congruences for a and b.",
        12: "The affine cipher is monoalphabetic, meaning letter frequencies remain correlated with English frequencies.",
        13: "If gcd(a, 26) > 1, multiple plaintexts map to the same ciphertext letter, making unambiguous decryption impossible.",
        14: "The inverse of 25 modulo 26 is 25, since 25 ≡ -1 mod 26 and (-1)² = 1."
    },
    22: {
        1: "The Vigenère cipher uses a keyword or phrase of length m repeated periodically.",
        2: "The encryption rule is c_i ≡ (p_i + k_{i mod m}) mod 26.",
        3: "The decryption rule is p_i ≡ (c_i - k_{i mod m}) mod 26.",
        4: "O is 14, R is 17. (14 + 17) mod 26 = 31 mod 26 = 5, which is F.",
        5: "The Vigenère square (tabula recta) consists of 26 rows of alphabets, each shifted by one position.",
        6: "It is polyalphabetic because the same plaintext letter encrypts to different ciphertext letters depending on its position.",
        7: "The Kasiski examination finds repeated strings in the ciphertext; the greatest common divisor of distances between repetitions reveals the key length.",
        8: "If key length is 1, the Vigenère cipher degenerates to a simple Caesar / shift cipher.",
        9: "F(5) - R(17) = -12 ≡ 14 (O). Decryption correctly reverses encryption.",
        10: "The Vigenère cipher defeated monoalphabetic frequency analysis because each letter has multiple possible ciphertext representations.",
        11: "The Friedman test uses the Index of Coincidence (IC) to estimate key length.",
        12: "If the key is as long as the message, completely random, and never reused, it becomes an unbreakable One-Time Pad (Vernam cipher).",
        13: "If the keyword is KEY (length 3), the 4th letter is encrypted with K (index 0 of the key).",
        14: "Polyalphabetic substitution flattens letter frequency peaks across multiple Caesar shifts."
    },
    23: {
        1: "The Hill cipher is based on matrix multiplication and linear algebra modulo 26.",
        2: "Block size m = 2 encrypts letters in consecutive digram pairs (two letters at a time).",
        3: "A key matrix K is invertible modulo 26 if and only if gcd(det(K), 26) = 1.",
        4: "det([[3,3],[2,5]]) = (3·5 - 3·2) = 15 - 6 = 9.",
        5: "gcd(9, 26) = 1, so 9 has an inverse modulo 26: 9 × 3 = 27 ≡ 1 mod 26.",
        6: "The decryption key is K⁻¹ = det(K)⁻¹ · adj(K) mod 26.",
        7: "K⁻¹ = 3 · [[5, -3], [-2, 3]] = [[15, -9], [-6, 9]] ≡ [[15, 17], [20, 9]] mod 26.",
        8: "K⁻¹ is [[15, 17], [20, 9]] modulo 26.",
        9: "H=7, I=8. [7, 8] · [[3,3],[2,5]] = [7·3+8·2, 7·3+8·5] = [37, 61] ≡ [11, 9] (L, J) or for specific matrix TC.",
        10: "A 3×3 Hill matrix encrypts blocks of 3 letters (trigrams) at a time.",
        11: "The Hill cipher is completely vulnerable to a known-plaintext attack: m known linearly independent plaintext-ciphertext pairs reveal the entire key matrix.",
        12: "det = 10 is not coprime to 26 (gcd(10, 26) = 2 ≠ 1), so no modular inverse exists.",
        13: "K · K⁻¹ ≡ I (mod 26), where I is the identity matrix.",
        14: "The Hill cipher achieves diffusion: changing a single plaintext character alters all characters in the ciphertext block."
    },
    24: {
        1: "A transposition cipher changes the positions of letters within a block without changing their identities.",
        2: "The key in a transposition cipher is a permutation σ of the set {1, 2, ..., m}.",
        3: "(3, 1, 4, 2) is a valid permutation of {1, 2, 3, 4} because each integer appears exactly once.",
        4: "For block size m = 5, there are 5! = 120 possible permutations.",
        5: "Under σ = (3, 1, 4, 2), the 1st letter moves to position 3.",
        6: "Applying the permutation rearranges letters into RPAI.",
        7: "The inverse of σ = (3, 1, 4, 2) is σ⁻¹ = (2, 4, 1, 3).",
        8: "Decryption requires applying the inverse permutation σ⁻¹ to each ciphertext block.",
        9: "Applying the inverse permutation to SWUE restores the original block WUSE.",
        10: "Letter frequencies are perfectly preserved under transposition because no letters are substituted.",
        11: "If the text length is not a multiple of block size m, pad the final block with dummy characters.",
        12: "The permutation cipher operates on blocks of m symbols, making it a block cipher."
    },
    25: {
        1: "A formal cryptosystem is defined as a 5-tuple (P, C, K, E, D).",
        2: "P denotes the Plaintext space: the set of all possible unencrypted messages.",
        3: "C denotes the Ciphertext space: the set of all possible encrypted messages.",
        4: "K denotes the Keyspace: the set of all permissible keys.",
        5: "E is the family of encryption transformations {E_k : k ∈ K}.",
        6: "D_k denotes the decryption transformation associated with key k.",
        7: "The core correctness condition is D_k(E_k(p)) = p for all plaintexts p and keys k.",
        8: "In a shift cipher over the English alphabet, the keyspace K is ℤ₂₆ = {0, 1, ..., 25}.",
        9: "The shift cipher encryption function is E_k(p) = (p + k) mod 26.",
        10: "The shift cipher decryption function is D_k(c) = (c - k) mod 26.",
        11: "Classical ciphers like Shift and Affine are private-key (symmetric) cryptosystems.",
        12: "In public-key cryptography, the encryption key is made publicly accessible to all users.",
        13: "In private-key cryptography, sender and receiver must securely share the secret key beforehand.",
        14: "Cryptanalysis is the study and practice of recovering plaintexts without knowledge of the secret key."
    },
    26: {
        1: "Public key cryptography is founded upon one-way trapdoor functions that are computationally easy to evaluate forward but infeasible to invert without the secret trapdoor.",
        2: "Fast modular exponentiation (repeated squaring) evaluates a^b mod n in O(log b) multiplications, whereas naive multiplication requires O(b).",
        3: "For any prime p, Euler's totient function is φ(p) = p - 1.",
        4: "Since 5 and 11 are prime, φ(55) = (5 - 1)(11 - 1) = 4 × 10 = 40.",
        5: "A modular multiplicative inverse of a modulo m exists if and only if gcd(a, m) = 1.",
        6: "3 × 4 = 12 ≡ 1 (mod 11), so the modular inverse of 3 modulo 11 is 4.",
        7: "By Fermat's Little Theorem, 3⁴ ≡ 1 (mod 5). 3¹⁷ = (3⁴)⁴ · 3¹ ≡ 1⁴ · 3 ≡ 3 (mod 5).",
        8: "For n users to communicate in symmetric pairs, n(n - 1)/2 shared keys are needed, creating an O(n²) key distribution bottleneck."
    },
    27: {
        1: "Diffie-Hellman relies on the computational intractability of the Discrete Logarithm Problem (DLP) in ℤ_p*.",
        2: "A primitive root modulo p generates all p - 1 non-zero elements of ℤ_p through its successive powers.",
        3: "Alice and Bob transmit public parameters (p, g) and public keys A = g^a mod p and B = g^b mod p openly over the insecure channel.",
        4: "A = 5⁶ mod 23 = 15625 mod 23 = 8.",
        5: "K = B^a mod p = 19⁶ mod 23 = 2.",
        6: "Pure unauthenticated Diffie-Hellman is vulnerable to a Man-in-the-Middle (MITM) attack because neither party authenticates their public key.",
        7: "The difficulty of computing g^{ab} mod p from g^a and g^b is the Computational Diffie-Hellman (CDH) problem.",
        8: "MITM attacks are mitigated by binding public keys to digital signatures or certificates verified through a PKI."
    },
    28: {
        1: "The security of RSA is founded on the computational hardness of factoring large composite integers n = pq.",
        2: "Modulus n = 3 × 11 = 33, and Euler's totient φ(n) = (3 - 1)(11 - 1) = 2 × 10 = 20.",
        3: "The public exponent e must satisfy 1 < e < φ(n) and gcd(e, φ(n)) = 1.",
        4: "d is the modular inverse of e modulo φ(n): 3d ≡ 1 (mod 20). 3 × 7 = 21 ≡ 1 (mod 20), so d = 7.",
        5: "RSA encryption computes ciphertext c ≡ m^e (mod n).",
        6: "RSA decryption computes plaintext m ≡ c^d (mod n).",
        7: "c = 2³ mod 33 = 8.",
        8: "RSA is deterministic because the same message m encrypted with key (n, e) always yields the identical ciphertext c.",
        9: "RSA correctness is proven using Euler's Totient Theorem: m^{φ(n)} ≡ 1 (mod n) when gcd(m, n) = 1, and CRT.",
        10: "Factoring n yields p and q, allowing immediate calculation of φ(n) and the private key d ≡ e⁻¹ mod φ(n)."
    },
    29: {
        1: "Public key cryptography is based on trapdoor one-way functions.",
        2: "φ(n) = (7 - 1)(13 - 1) = 6 × 12 = 72.",
        3: "In RSA, the private key is d where ed ≡ 1 (mod φ(n)).",
        4: "In Diffie-Hellman, the shared secret key is K = g^{ab} mod p.",
        5: "ElGamal is probabilistic because every encryption uses a fresh random ephemeral key k.",
        6: "ElGamal ciphertext consists of two group elements (c₁, c₂), doubling the message length (2:1 ratio).",
        7: "Diffie-Hellman is strictly a key-agreement protocol; it does not provide arbitrary message encryption directly.",
        8: "The Extended Euclidean Algorithm finds Bézout coefficients that solve ed + kφ(n) = 1 to find modular inverse d."
    }
}
