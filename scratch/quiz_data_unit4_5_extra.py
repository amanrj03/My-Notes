# -*- coding: utf-8 -*-
"""
Full question definitions for Modules 26, 27, 28, and 29
to guarantee 100% interactive quiz coverage.
"""

MODULE_26_QUESTIONS = [
    {
        "num": 1,
        "text": "What mathematical construct forms the foundational requirement for public key cryptography?",
        "options": ["Symmetric permutation tables", "Trapdoor one-way functions", "Linear congruential generators", "Direct substitution tables"]
    },
    {
        "num": 2,
        "text": "What is the time complexity of naive modular exponentiation a^b mod n compared to repeated squaring?",
        "options": ["O(log b) vs O(b)", "O(b) vs O(log b)", "O(n) vs O(log n)", "O(b²) vs O(b)"]
    },
    {
        "num": 3,
        "text": "For any prime integer p, what is Euler's totient function φ(p)?",
        "options": ["p − 1", "p + 1", "p / 2", "2^p − 1"]
    },
    {
        "num": 4,
        "text": "If p = 5 and q = 11 are distinct primes, what is φ(pq)?",
        "options": ["55", "50", "40", "44"]
    },
    {
        "num": 5,
        "text": "Under what condition does an integer a possess a modular multiplicative inverse modulo m?",
        "options": ["gcd(a, m) = 1", "a is prime", "m divides a", "a > m"]
    },
    {
        "num": 6,
        "text": "What is the modular multiplicative inverse of 3 modulo 11?",
        "options": ["3", "7", "4", "9"]
    },
    {
        "num": 7,
        "text": "Compute 3¹⁷ mod 5 using Fermat's Little Theorem.",
        "options": ["1", "2", "3", "4"]
    },
    {
        "num": 8,
        "text": "How many pairwise secret keys are required for n users in symmetric private-key cryptography?",
        "options": ["n", "n(n − 1) / 2", "2^n", "n!"]
    }
]

MODULE_27_QUESTIONS = [
    {
        "num": 1,
        "text": "On which computationally hard problem does the Diffie-Hellman key exchange rely?",
        "options": ["The Discrete Logarithm Problem (DLP)", "Integer Factorization Problem", "Shortest Vector Problem", "Subset Sum Problem"]
    },
    {
        "num": 2,
        "text": "What is a primitive root modulo prime p?",
        "options": ["The smallest prime dividing p − 1", "A generator whose powers modulo p yield all non-zero residues {1, ..., p-1}", "A root of a polynomial with prime coefficients", "Any prime factor of p"]
    },
    {
        "num": 3,
        "text": "In Diffie-Hellman, which parameters are transmitted openly over the public channel?",
        "options": ["Domain parameters (p, g) and public keys (A, B)", "Private secrets (a, b)", "The shared session key K directly", "The discrete logarithm of the key"]
    },
    {
        "num": 4,
        "text": "If p = 23, g = 5, and Alice chooses private secret a = 6, what is Alice's public key A?",
        "options": ["5", "8", "12", "19"]
    },
    {
        "num": 5,
        "text": "If Bob's public key is B = 19, Alice's secret is a = 6, and p = 23, what is shared key K = B^a mod p?",
        "options": ["1", "5", "2", "9"]
    },
    {
        "num": 6,
        "text": "What major security vulnerability affects basic unauthenticated Diffie-Hellman?",
        "options": ["Brute force key exhaustion", "Man-in-the-Middle (MITM) attack", "Known-plaintext attack", "Frequency analysis"]
    },
    {
        "num": 7,
        "text": "The difficulty of computing g^(ab) mod p given only g^a mod p and g^b mod p is known as:",
        "options": ["Discrete Logarithm Problem", "Computational Diffie-Hellman (CDH) problem", "RSA factoring problem", "Knapsack problem"]
    },
    {
        "num": 8,
        "text": "How can Diffie-Hellman be authenticated to prevent MITM attacks?",
        "options": ["Digital signatures / PKI certificates", "Increasing the prime p to 3000 bits without signatures", "Re-running the exchange twice", "Using Caesar cipher on the keys"]
    }
]

MODULE_28_QUESTIONS = [
    {
        "num": 1,
        "text": "The cryptographic security of RSA is primarily founded upon the hardness of:",
        "options": ["Discrete Logarithms", "Integer Factorization of large composites n = pq", "Solving non-linear equations", "Permutation matrix inversion"]
    },
    {
        "num": 2,
        "text": "If p = 3 and q = 11, what are the modulus n and Euler's totient φ(n)?",
        "options": ["n = 33, φ(n) = 20", "n = 33, φ(n) = 30", "n = 14, φ(n) = 20", "n = 33, φ(n) = 22"]
    },
    {
        "num": 3,
        "text": "Which condition must the public encryption exponent e satisfy in RSA?",
        "options": ["e must be a factor of n", "1 < e < φ(n) and gcd(e, φ(n)) = 1", "e must be an even integer", "e = p + q"]
    },
    {
        "num": 4,
        "text": "Given φ(n) = 20 and public exponent e = 3, what is the private decryption key d?",
        "options": ["3", "5", "7", "9"]
    },
    {
        "num": 5,
        "text": "What is the encryption formula in RSA for message m with public key (n, e)?",
        "options": ["c ≡ m^e (mod n)", "c ≡ e^m (mod n)", "c ≡ me (mod n)", "c ≡ (m + e) (mod n)"]
    },
    {
        "num": 6,
        "text": "What is the decryption formula in RSA for ciphertext c with private key d?",
        "options": ["m ≡ cd (mod n)", "m ≡ c^d (mod n)", "m ≡ d^c (mod n)", "m ≡ (c − d) (mod n)"]
    },
    {
        "num": 7,
        "text": "If n = 33 and e = 3, encrypt the plaintext message m = 2.",
        "options": ["8", "6", "11", "16"]
    },
    {
        "num": 8,
        "text": "Why is standard textbook RSA described as a deterministic cryptosystem?",
        "options": ["It uses symmetric secret keys", "The same plaintext message always encrypts to the exact same ciphertext under key (n, e)", "It does not require modular arithmetic", "It cannot be decrypted"]
    },
    {
        "num": 9,
        "text": "Which mathematical theorem provides the proof of correctness for RSA decryption m^(ed) ≡ m (mod n)?",
        "options": ["Wilson's Theorem", "Pythagorean Theorem", "Euler's Totient Theorem & Chinese Remainder Theorem", "Bézout's Lemma alone"]
    },
    {
        "num": 10,
        "text": "If an attacker can factor modulus n into primes p and q, how is the system compromised?",
        "options": ["The attacker only discovers p", "The attacker can compute φ(n) = (p−1)(q−1) and derive private key d ≡ e⁻¹ mod φ(n)", "The attacker still cannot decrypt messages", "The attacker only changes the public key"]
    }
]

MODULE_29_QUESTIONS = [
    {
        "num": 1,
        "text": "Public key cryptography is founded upon which mathematical construct?",
        "options": ["Symmetric key substitution", "Trapdoor one-way functions", "The Caesar shift rule", "Linear regression"]
    },
    {
        "num": 2,
        "text": "If p = 7 and q = 13, what is Euler's totient φ(n) where n = pq?",
        "options": ["91", "84", "72", "78"]
    },
    {
        "num": 3,
        "text": "In the RSA cryptosystem with public key (n, e), what is the private key?",
        "options": ["p alone", "q alone", "d such that ed ≡ 1 (mod φ(n))", "φ(n) alone"]
    },
    {
        "num": 4,
        "text": "In the Diffie-Hellman protocol with base g and modulus p, what is the shared secret key?",
        "options": ["g^a + g^b mod p", "g^(ab) mod p", "g^(a+b) mod p", "ab mod p"]
    },
    {
        "num": 5,
        "text": "Which public key cryptosystem is probabilistic (produces different ciphertexts for identical messages)?",
        "options": ["Textbook RSA", "ElGamal", "Affine Cipher", "Hill Cipher"]
    },
    {
        "num": 6,
        "text": "What is the ciphertext expansion ratio in the ElGamal cryptosystem?",
        "options": ["1:1 (no expansion)", "2:1 (ciphertext consists of pair (c₁, c₂))", "4:1", "1:2 (compressed)"]
    },
    {
        "num": 7,
        "text": "What is the primary difference in function between Diffie-Hellman and ElGamal?",
        "options": ["Diffie-Hellman uses prime numbers; ElGamal does not", "Diffie-Hellman is strictly key agreement; ElGamal provides asymmetric message encryption", "ElGamal is symmetric; Diffie-Hellman is asymmetric", "Diffie-Hellman can encrypt arbitrary files"]
    },
    {
        "num": 8,
        "text": "Which algorithm is used to compute modular inverse private keys in both RSA and Affine ciphers?",
        "options": ["Sieve of Eratosthenes", "Extended Euclidean Algorithm", "Trial division", "Fermat primality test"]
    }
]

EXTRA_MODULE_QUESTIONS = {
    26: MODULE_26_QUESTIONS,
    27: MODULE_27_QUESTIONS,
    28: MODULE_28_QUESTIONS,
    29: MODULE_29_QUESTIONS
}
